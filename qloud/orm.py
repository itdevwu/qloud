# Copyright (c) 20222 Zhenglong WU
import config
from job import Job, JobIn

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel


class Database:
    def __init__(self) -> None:
        self.running_jobs = 0

        self.database = databases.Database(config.DATABASE_URL)

        self.metadata = sqlalchemy.MetaData()

        self.jobs = sqlalchemy.Table(
            "jobs",
            self.metadata,
            sqlalchemy.Column("j_id", sqlalchemy.Integer, primary_key=True),
            sqlalchemy.Column("j_num", sqlalchemy.Integer),
            sqlalchemy.Column("j_iter", sqlalchemy.Integer),
            sqlalchemy.Column("j_status", sqlalchemy.Integer),
            sqlalchemy.Column("j_res", sqlalchemy.Integer),
            sqlite_autoincrement=True,
        )

        self.engine = sqlalchemy.create_engine(
            config.DATABASE_URL, connect_args={"check_same_thread": False}
        )
        self.metadata.create_all(self.engine)

    async def create_job(self, job: JobIn):
        query = self.jobs.insert().values(text=job.text, completed=job.completed)
        last_record_id = await self.database.execute(query)
        return {**job.dict(), "j_id": last_record_id}
