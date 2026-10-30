def login(username, password):
    """Simple demonstration login function."""
    if username == "admin" and password == "admin123":
        return "Login successful"
    return "Invalid username or password"


def main():
    print("Welcome to the DevOps practical application!")
    print(login("admin", "admin123"))


if __name__ == "__main__":
    main()
