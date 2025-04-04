def login(username, password):
    # Replace this with actual user data validation logic
    if username == "admin" and password == "password123":
        return "Login successful!"
    else:
        return "Login failed. Please check your credentials."

# Example usage
if __name__ == "__main__":
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    print(login(user, pwd))