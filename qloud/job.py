# Copyright (c) 20222 Zhenglong WU

from datetime import datetime
import random
import json

from pydantic import BaseModel


def generate_id():
    now = datetime.now()
    random_suffix = "".join(random.choice("0123456789") for i in range(6))
    return f"{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}{now.microsecond}-{random_suffix}"


class JobMem:
    def __init__(
        self, job_id: str, job_num: int, job_iter: int, job_status: int, job_res: dict
    ) -> None:
        self.job_id = job_id
        self.job_num = job_num
        self.job_iter = job_iter
        self.job_status = job_status
        self.job_res = job_res
        self.x_axis = []
        self.y_axis = []

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def id(self) -> str:
        return self.job_id

    def number(self) -> int:
        return self.job_num

    def experiment_iter(self) -> int:
        return self.job_iter

    def status(self) -> int:
        return self.job_status

    def result(self) -> dict:
        return self.job_res


class JobModel(BaseModel):

    job_id: str
    job_num: int
    job_iter: int
    job_status: int
    job_res: dict

    @classmethod
    def __init__(
        cls, job_id: str, job_num: int, job_iter: int, job_status: int, job_res: dict
    ) -> None:
        cls.job_id = job_id
        cls.job_num = job_num
        cls.job_iter = job_iter
        cls.job_status = job_status
        cls.job_res = job_res

    @classmethod
    def __init__(cls, job: JobMem) -> None:
        cls.job_id = job.job_id
        cls.job_num = job.job_num
        cls.job_iter = job.job_iter
        cls.job_status = job.job_status
        cls.job_res = job.job_res

    @classmethod
    def id(cls) -> str:
        return cls.job_id

    @classmethod
    def number(cls) -> int:
        return cls.job_num

    @classmethod
    def experiment_iter(cls) -> int:
        return cls.job_iter

    @classmethod
    def status(cls) -> int:
        return cls.job_status

    @classmethod
    def result(cls) -> dict:
        return cls.job_res
