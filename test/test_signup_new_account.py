def randomize_username(prefix, max_len=10):
    import random, string
    symbols = string.ascii_letters
    return prefix + "".join(random.choice(symbols) for i in range(max_len))


def test_signup_new_account(app):
    username = randomize_username('user_')
    email = username+'@localhost'
    password = 'test'
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, email, password)
    app.session.login(username, password)
    assert app.session.is_logged_in_as(username)
    app.session.logout()