# Copyright (c) 20222 Zhenglong WU

class Job:
    def __init__(self, job_id: str, job_status: int, job_res: dict) -> None:
        self.job_id = job_id
        self.job_status = job_status
        self.job_res = job_res

    def id(self) -> str:
        return self.job_id

    def status(self) -> int:
        return self.job_status

    def result(self) -> dict:
        return self.job_res
