from fastapi import FastAPI

app = FastAPI()

# 웹훅 엔드포인트
@app.post("/webhook")
async def process_webhook(data: dict):
    # 여기에서 웹훅 데이터를 처리하고 IoT 기기로 명령을 전송합니다.
    # data에는 음성 입력 또는 사용자의 요청에 관한 정보가 포함됩니다.
    # 처리한 결과를 반환하거나 다른 작업을 수행합니다.
   
    response_message = {"message": "웹훅이 성공적으로 처리되었습니다."}
    return response_message

# 서버 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)