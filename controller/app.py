from fastapi import FastAPI, Depends, status
from service.serializers.time_scheduler_dto import TimeSchedulerDTO
from service.time_scheduler_service import TimeSchedulerService

app = FastAPI(dependencies=[Depends(TimeSchedulerService)])


@app.post("/time-table", status_code=status.HTTP_201_CREATED)
async def create_time_table(time_scheduler: TimeSchedulerDTO,
                            time_scheduler_service: TimeSchedulerService = Depends()):
    time_scheduler_service.create_time_table(time_scheduler)


@app.get("/health-check")
async def health_check():
    return {"status": "OK!"}
