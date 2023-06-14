import httpx
from prefect import flow, task


@task
def fetch_cat_fact():
    return httpx.get("https://catfact.ninja/fact?max_length=140").json()["fact"]


@task(persist_result=True)
def formatting(fact: str):
    return fact.title()


@flow
def pipe(name: str):
    fact = fetch_cat_fact()
    formatted_fact = formatting(fact)
    print("test repo")


if __name__ == "__main__":
    pipe(name)
