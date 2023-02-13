from infrastructure.communication.rest_api import app  # noqa

if __name__ == '__main__':
    import uvicorn as uvicorn

    uvicorn.run("main:app", reload=True)
