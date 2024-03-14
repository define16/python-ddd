from fastapi import FastAPI

from src.infrastructure.fastapi.router import item, admin


class ApiProvider:
    def construct(self, env):
        api = FastAPI()
        if env == "admin":
            api.include_router(admin.router)
            # api.add_middleware(
            #     CORSMiddleware,
            #     allow_origins=settings.BACKEND_CORS_ORIGINS,
            #     allow_credentials=True,
            #     allow_methods=["*"],
            #     allow_headers=["*"],
            # )
        else:
            api.include_router(item.router)
            # api.add_middleware(
            #     CORSMiddleware,
            #     allow_origins=settings.BACKEND_CORS_ORIGINS,
            #     allow_credentials=True,
            #     allow_methods=["*"],
            #     allow_headers=["*"],
            # )
        return api
