from pydantic import BaseModel
from . import api_router


class SiteUrl(BaseModel):
    url: str


class Question(BaseModel):
    question: str


@api_router.post("/scrape")
async def scrape(site_url: SiteUrl):
    """
    Endpoint that creates a Celery task for scraping a given site.
    """
    # Code to create Celery tasks goes here
    return {"message": "Successfully!"}


@api_router.post("/answer")
async def answer_question(question: Question):
    """
    Endpoint that answers a question based on the most similar context.
    """
    return {"answer": "answer"}
