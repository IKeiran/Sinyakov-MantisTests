def test_login(app):
    app.session.login_as("administrator", "root")
    user = app.session.get_logged_user()
    print(user)
    assert app.session.is_logged_in_as("administrator")