from loggers.logger_factory import LoggerFactory

from fastapi import FastAPI

app = FastAPI()
main_logger = LoggerFactory.get_logger('main')


@app.get("/")
async def root():
    main_logger.info("Python app is logging to file. 123")
    return {"message": "Hello World"}
