# Copyright (c) 20222 Zhenglong WU

import os
import time
import ast

import config
from job import JobMem, generate_id

from fastapi import BackgroundTasks, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class CreateJobReq(BaseModel):
    number: int
    experiment_iter: int


running_jobs: int
jobs: dict

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def execute_jobs(id: str):
    global running_jobs
    while running_jobs >= config.MAX_RUNNING_JOB:
        time.sleep(1)
        pass

    running_jobs += 1
    jobs[id].job_status = 1

    print(f"Running job {id}")
    os.system(
        f"python plain_output.py {jobs[id].number()} {jobs[id].experiment_iter()} {id}"
    )
    f = open(f"{id}.txt", "r")
    res: dict = ast.literal_eval(str(f.read()))
    os.system(f"rm {id}.txt")
    print(f"Job {id} finished!")
    print(res)

    max_val = max(list(res.keys()))
    for i in range(max_val + 1):
        if i in res:
            jobs[id].x_axis.append(i)
            jobs[id].y_axis.append(res[i])
        else:
            jobs[id].x_axis.append(i)
            jobs[id].y_axis.append(0)
    jobs[id].job_res = res
    jobs[id].job_status = 2
    running_jobs -= 1


@app.on_event("startup")
async def startup():
    global running_jobs
    global jobs
    running_jobs = 0
    jobs = {}


@app.on_event("shutdown")
async def shutdown():
    pass


@app.get("/")
async def root():
    return {
        "message": f"Hello Qloud {config.QLOUD_VERSION}, one of {config.QLOUD_AUTHOR}'s opensource projects!"
    }


@app.get("/job/{id}")
async def query_job(id: str):
    res = {"error": "nothing found"}
    if id in jobs:
        return jobs[id]
    return res


@app.post("/createjob")
async def create_job(req: CreateJobReq, background_tasks: BackgroundTasks):
    res = {"result": "error", "msg": "unknown reason"}
    if req.number < 1:
        res = {"result": "error", "msg": "number must greater than 1"}
    if req.experiment_iter < 1:
        res = {"result": "error", "msg": "experiment iterations must more than 1"}
    if req.experiment_iter > config.MAX_EXPERIMENT_ITER:
        res = {
            "result": "error",
            "msg": f"experiment iterations mustn't more than {config.MAX_EXPERIMENT_ITER}",
        }

    id = generate_id()
    job = JobMem(id, req.number, req.experiment_iter, 0, {})
    jobs[id] = job
    background_tasks.add_task(execute_jobs, id)

    res = {"result": "ok", "msg": f"{id}"}

    return res
