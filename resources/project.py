from pydo import Client
import requests

class Project:
    def __init__(self,token,name):
        self.token=token
        self.name=name
        self.client = Client(token=token)        
        self.project_list=self.client.projects.list()['projects']
        self.exists,self.project_id=self._check_if_exists()
    def _check_if_exists(self):
        exists=False
        project_id=False
        for p in self.project_list:
            if p['name']==self.name:
                exists=True
                project_id=p['id']
        return exists,project_id
    def delete(self):
        #Native method casts error. use requests instead
        url=f"https://api.digitalocean.com/v2/projects/{self.project_id}"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        response=requests.delete(url=url,headers=headers)
        if response.status_code==204:
            print(f"SUCCESSFULLY DELETED PROJECT {self.name}")
        return response.status_code
    def create(self):
        body = {
            #"created_at": "2020-02-20 00:00:00",  # Optional. A time value given in
            #"description": "str",  # Optional. The description of the project. The
            #  maximum length is 255 characters.
            #"environment": "str",  # Optional. The environment of the project's
            #  resources. Known values are: "Development", "Staging", and "Production".
            #"id": "str",  # Optional. The unique universal identifier of this project.
            "name": "sendbox",  # Optional. The human-readable name for the project. The
            #  maximum length is 175 characters and the name must be unique.
            #"owner_id": 0,  # Optional. The integer id of the project owner.
            #"owner_uuid": "str",  # Optional. The unique universal identifier of the
            #  project owner.
            "purpose": "Just trying out DigitalOcean",  # Optional. The purpose of the project. The maximum length
            #  is 255 characters. It can have one of the following values:   * Just trying out
            #  DigitalOcean * Class project / Educational purposes * Website or blog * Web
            #  Application * Service or API * Mobile Application * Machine learning / AI / Data
            #  processing * IoT * Operational / Developer tooling  If another value for purpose
            #  is specified, for example, "your custom purpose", your purpose will be stored as
            #  ``Other: your custom purpose``.
            #"updated_at": "2020-02-20 00:00:00"  # Optional. A time value given in
            #  ISO8601 combined date and time format that represents when the project was
            #  updated.
        }
        if self.exists:
            print("PROJECT ALREADY EXISTS")
            return self.project_id
        else:
            try:
                self.client.projects.create(body)
                self.project_list=self.client.projects.list()['projects']
                self.exists,self.project_id=self._check_if_exists()
                return self.project_id
            except:
                print("ERROR: COULD NOT CREATE PROJECT")
                return False



