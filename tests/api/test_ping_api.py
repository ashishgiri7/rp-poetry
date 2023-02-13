def test_read_main(client):
    """Test Case for Basic API"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hey, It is me Ash"}
