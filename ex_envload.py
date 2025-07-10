from dotenv import load_dotenv
import os

load_dotenv()  # ← .env가 같은 폴더에 있으면 경로 생략 가능

api_key = os.getenv("UPSTAGE_API_KEY")
print("🚀 API 키:", api_key)