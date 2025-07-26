def test_health():
    from app import create_app
    app = create_app()
    client = app.test_client()
    res = client.get("/health")
    assert res.status_code == 200
