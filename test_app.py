from app import login

def test_login_success():
    result = login("admin", "admin123")
    assert result == "Login successful"

def test_login_failure():
    result = login("user", "wrong")
    assert result == "Invalid username or password"