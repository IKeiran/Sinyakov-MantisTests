from model.Project import Project

def test_project_create(app):
    project = Project.generate_random()
    print('fgf')
    app.session.login_as("administrator", "root")
    app.project.create(user_password="root", project=project)
    print('')
