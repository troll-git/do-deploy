from pydo import Client
from resources.project import Project
class App:
    def __init__(self,token,appname,projectname):
        self.token=token
        self.appname=appname
        self.client = Client(token=token) 
        self.projectname=projectname
        self.project=Project(self.token,self.projectname)
        self.exists,self.appproperties=self._check_if_exists()
    def _getallApps(self):
        apps=self.client.apps.list()
        return apps
    def _getprojectresources(self):
        resp = self.client.projects.list_resources(project_id=self.project.project_id)
        try:
            id_list=[]
            for r in resp['resources']:
                id_list.append(r['urn'].split(":")[-1])
            return id_list
        except:
            print("PROJECT HAS NO RESOURCES")
            return []

    def _check_if_exists(self):
        project_id=self.project.project_id
        project_resources=self._getprojectresources()
        exists=False
        d=False
        if project_id:
            for d in self._getallApps()['apps']:
                if d['spec']['name']==self.appname:
                    if d['id'] in project_resources:
                        exists=True
        return exists,d
    def create_app(self):
        body={
        "spec": {
            "name": f"{self.appname}",
            "region": "fra1",
            "services": [
                {
                    "name": "api",
                    "github": {
                    "branch": "main",  # Optional. The name of the
                    "repo": "troll-git/geoserver-do"  # Optional. The name of the
                    #  repo in the format owner/repo. Example:
                    #  ``digitalocean/sample-golang``.
                    },
                    "dockerfile_path": "Dockerfile",
                    "source_dir": "/",
                    "instance_size_slug": "apps-s-1vcpu-2gb",
                    "instance_count": 1,
                    "http_port": 8080
                    #"run_command": "bin/api",
                    #"environment_slug": "node-js",
                    #"instance_count": 2,
                    #"instance_size_slug": "apps-s-1vcpu-0.5gb",
                    #"routes": [],
                }
            ],
        },
        "project_id":f"{self.project.project_id}"
        }
        if not self.exists:
            try:
                create_resp = self.client.apps.create(body)
                self.exists,self.appproperties=self._check_if_exists()
                return create_resp
            except:
                return False
        
