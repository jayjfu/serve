# pylint: disable=redefined-builtin
# pylint: disable=missing-docstring
from datetime import datetime
import json
from workflow_archiver import __version__


class Manifest(object):
    """
    The main manifest object which gets written into the workflow archive as MANIFEST.json
    """

    def __init__(self, workflow):

        self.creation_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.workflow = workflow
        self.archiver_version = __version__
        self.manifest_dict = self.__to_dict__()

    def __to_dict__(self):
        manifest_dict = dict()

        manifest_dict['createdOn'] = self.creation_time

        manifest_dict['workflow'] = self.workflow.__to_dict__()

        if self.archiver_version is not None:
            manifest_dict['archiverVersion'] = self.archiver_version

        return manifest_dict

    def __str__(self):
        return json.dumps(self.manifest_dict, indent=2)

    def __repr__(self):
        return json.dumps(self.manifest_dict, indent=2)