from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + 'api/soap/mantisconnect.php?wsdl')
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        def convert(mnts_project):
            result = Project(name=mnts_project.name, id=mnts_project.id, status=mnts_project.status.name,
                             view_status=mnts_project.view_state.name, description=mnts_project.description)
            return result
        client = Client(self.app.base_url + 'api/soap/mantisconnect.php?wsdl')
        try:
            result = client.service.mc_projects_get_user_accessible(username, password)
            print(result)
            return list(map(convert,result))
        except WebFault:
            return None
