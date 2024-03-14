import uvicorn
from src.infrastructure.fastapi.api_provider import ApiProvider


if __name__ == '__main__':
    api_provider = ApiProvider()
    api = api_provider.construct("admin")
    uvicorn.run(api, host="0.0.0.0", port=8000)  # 여기 옵션은 뭐지 ? reload = True, workers = 1
