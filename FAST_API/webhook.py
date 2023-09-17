from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# POST 요청을 처리하는 웹훅 엔드포인트
@app.post("/webhook")
async def webhook_handler(data: dict):
    try:
        # 여기에서 웹훅 데이터를 처리하고 원하는 작업을 수행합니다.
       
        # 예제: 웹훅 데이터를 출력
        print("Received webhook data:", data)
       
        # 여기에 웹훅 데이터를 기반으로 원하는 로직을 구현합니다.
        # 예를 들어, IoT 기기로 명령을 전달하거나 다른 서비스와 통합할 수 있습니다.
       
        # 웹훅 요청을 외부 서버로 다시 전송
        response = requests.post("https://webhook.site/6490d166-8c99-4753-9294-e417feeb6c4c", json=data)
       
        if response.status_code == 200:
            return {"message": "Webhook received and processed successfully"}
        else:
            return {"message": "Webhook processing failed"}
   
    except Exception as e:
        raise HTTPException(status_code=500, detail="Webhook processing error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

