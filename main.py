from fastapi import FastAPI
import boto3
import json
import os
from pydantic import BaseModel
from datetime import datetime
from enum import Enum
import psycopg2

app = FastAPI()


class SupportTicket(BaseModel):
    ticket_id: int
    title: str
    description: str
    caller: str
    caller_email: str
    caller_phone_num: str
    caller_contact_preference: str
    status: str
    category: str
    reason: str
    support_assigned: str
    is_assigned: bool
    support_closed_reason: str
    caller_closed_reason: str
    date_created: datetime
    date_modified: datetime
    date_assigned: datetime
    date_opened: datetime
    date_closed: datetime


# Create an AWS Secrets Manager client
client = boto3.client("secretsmanager")

# Retrieve the database credentials from AWS Secrets Manager
response = client.get_secret_value(SecretId=os.getenv("db_secrets_key"))
secret_data = json.loads(response["SecretString"])

DB_HOST = secret_data["host"]
DB_PORT = int(secret_data["port"])
DB_NAME = secret_data["name"]
DB_USER = secret_data["username"]
DB_PASSWORD = secret_data["password"]


@app.get("/")
async def root():
    return {"message": "Welcome to the Support Center API for Script Casters"}


@app.get("/customer/ticket/{ticket_id}")
async def get_support_ticket(_self, sso_id: str, ticket_id: str):
    return {"message": f"Hello {ticket_id}"}


@app.get("/customer/tickets")
async def get_support_tickets(_self, sso_id: str, ticket_status: str = "OPEN"):
    return {"message": f"Hello {ticket_status}"}


@app.post("/customer/ticket")
async def create_support_ticket(_self, ticket_request_data):
    return {"message": f"received"}


@app.put("/customer/ticket/{ticket_id}")
async def edit_support_ticket(_self, ticket_request_data):
    return {"message": f"received"}
