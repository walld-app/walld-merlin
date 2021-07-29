from aku_aku.app import app


@app.get("/api/service/healthcheck")
def healthcheck():
    return {}
