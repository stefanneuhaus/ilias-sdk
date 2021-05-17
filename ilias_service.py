import json
import logging

from zeep import Client

from ilias_file import IliasFile
from utils import read_binary_file


class IliasService:
    # uses zeep as a SOAP client, see https://github.com/mvantellingen/python-zeep

    def __init__(self, service_configuration_filename):
        self.__configure_logging()
        with open(service_configuration_filename, 'r') as service_configuration_file:
            service_configuration = json.load(service_configuration_file)
        wsdl_url = service_configuration['wsdlUrl']
        self.service = Client(wsdl_url).service
        self.client_id = service_configuration['clientId']
        self.username = service_configuration['credentials']['username']
        self.password = service_configuration['credentials']['password']
        self.sid = None

    def __getattr__(self, name):
        # proxy all requests to the SOAP client's service
        return getattr(self.service, name)

    def login(self):
        self.sid = self.service.login(client=self.client_id, username=self.username, password=self.password)
        logging.info("Successfully logged in to %s as %s.", self.client_id, self.username)
        return self.sid

    def logout(self):
        if self.sid is not None:
            self.service.logout(self.sid)
            logging.info('Logged out.')

    def process_tasks(self, tasks_filename):
        logging.info('Processing tasks in %s', tasks_filename)
        with open(tasks_filename, 'r', encoding='utf-8') as tasks_file:
            tasks = json.load(tasks_file)
        for task in tasks:
            self.__process_task(task)
        logging.info('Done.')

    def update_file(self, ref_id, filename, title=None):
        ilias_file = IliasFile(filename, content=read_binary_file(filename), title=title)
        self.service.updateFile(sid=self.sid, ref_id=ref_id, xml=ilias_file.to_string())

    def __configure_logging(self):
        logging.basicConfig(format='%(message)s', level=logging.INFO)

    def __process_task(self, task):
        logging.info('Processing %s', task)
        task_type = task['type']
        if task_type == "updateFile":
            ref_id = task['refId']
            filename = task['fileName']
            title = task.get('title')
            self.update_file(ref_id, filename, title)
        else:
            logging.warning("Ignoring task with unsupported type '%s'.", task_type)
