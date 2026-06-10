"""대전 날씨를 조회해서 이메일로 발송하는 스크립트.

GitHub Actions에서 매일 14:00 KST에 실행된다.
필요한 환경변수:
  MAIL_USERNAME - Gmail 주소 (발신 계정)
  MAIL_PASSWORD - Gmail 앱 비밀번호
  MAIL_TO       - 수신자 주소
"""

import json
import os
import smtplib
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from email.mime.text import MIMEText
from email.utils import formataddr

# 대전광역시 좌표
LATITUDE = 36.3504
LONGITUDE = 127.3845

API_URL = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={LATITUDE}&longitude={LONGITUDE}"
    "&current=temperature_2m,apparent_temperature,relative_humidity_2m,"
    "weather_code,wind_speed_10m"
    "&daily=temperature_2m_max,temperature_2m_min,"
    "precipitation_probability_max,weather_code"
    "&timezone=Asia%2FSeoul&forecast_days=2"
)

# WMO weather code -> 한국어 설명
WEATHER_CODES = {
    0: "맑음 ☀️",
    1: "대체로 맑음 🌤️",
    2: "구름 조금 ⛅",
    3: "흐림 ☁️",
    45: "안개 🌫️",
    48: "착빙 안개 🌫️",
    51: "약한 이슬비 🌦️",
    53: "이슬비 🌦️",
    55: "강한 이슬비 🌧️",
    56: "약한 어는 이슬비 🌧️",
    57: "어는 이슬비 🌧️",
    61: "약한 비 🌧️",
    63: "비 🌧️",
    65: "강한 비 🌧️",
    66: "약한 어는 비 🌧️",
    67: "어는 비 🌧️",
    71: "약한 눈 🌨️",
    73: "눈 🌨️",
    75: "강한 눈 ❄️",
    77: "싸락눈 ❄️",
    80: "약한 소나기 🌦️",
    81: "소나기 🌧️",
    82: "강한 소나기 ⛈️",
    85: "약한 소낙눈 🌨️",
    86: "강한 소낙눈 ❄️",
    95: "뇌우 ⛈️",
    96: "뇌우(약한 우박) ⛈️",
    99: "뇌우(강한 우박) ⛈️",
}


def describe(code: int) -> str:
    return WEATHER_CODES.get(code, f"알 수 없음(코드 {code})")


def fetch_weather() -> dict:
    with urllib.request.urlopen(API_URL, timeout=30) as resp:
        return json.load(resp)


def build_message(data: dict) -> tuple[str, str]:
    kst = timezone(timedelta(hours=9))
    today = datetime.now(kst)

    cur = data["current"]
    daily = data["daily"]

    subject = (
        f"[대전 날씨] {today:%m/%d} {describe(cur['weather_code'])} "
        f"{cur['temperature_2m']:.0f}°C"
    )

    body = "\n".join(
        [
            f"🏙️ 대전광역시 날씨 — {today:%Y년 %m월 %d일 (%a) %H:%M} 기준",
            "",
            "■ 현재",
            f"  상태: {describe(cur['weather_code'])}",
            f"  기온: {cur['temperature_2m']}°C (체감 {cur['apparent_temperature']}°C)",
            f"  습도: {cur['relative_humidity_2m']}%",
            f"  바람: {cur['wind_speed_10m']} km/h",
            "",
            "■ 오늘",
            f"  상태: {describe(daily['weather_code'][0])}",
            f"  최저/최고: {daily['temperature_2m_min'][0]}°C / {daily['temperature_2m_max'][0]}°C",
            f"  강수확률(최대): {daily['precipitation_probability_max'][0]}%",
            "",
            "■ 내일",
            f"  상태: {describe(daily['weather_code'][1])}",
            f"  최저/최고: {daily['temperature_2m_min'][1]}°C / {daily['temperature_2m_max'][1]}°C",
            f"  강수확률(최대): {daily['precipitation_probability_max'][1]}%",
            "",
            "— 자동 발송 (Open-Meteo / GitHub Actions)",
        ]
    )
    return subject, body


def send_mail(subject: str, body: str) -> None:
    username = os.environ["MAIL_USERNAME"]
    password = os.environ["MAIL_PASSWORD"]
    to_addr = os.environ["MAIL_TO"]

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = formataddr(("대전 날씨봇", username))
    msg["To"] = to_addr

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30) as smtp:
        smtp.login(username, password)
        smtp.send_message(msg)


def main() -> None:
    data = fetch_weather()
    subject, body = build_message(data)
    print(body)
    if os.environ.get("DRY_RUN") == "1":
        print("\n(DRY_RUN=1: 메일 발송 생략)")
        return
    send_mail(subject, body)
    print("\n메일 발송 완료")


if __name__ == "__main__":
    sys.exit(main())
