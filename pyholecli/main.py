from fabric.main import Fab
from fabric import Config, Executor
from invoke import Collection
from pyholecli import tasks
from pyholecli._version import __version__ as version


class PyholeCLI(Fab):
    default_host = 'pi.hole'

    def _set_default_args(self):
        if not self.args['hosts'].value:
            self.args['hosts'].value = self.default_host

    def update_config(self):
        self._set_default_args()
        super().update_config()


program = PyholeCLI(
    name='PyholeCLI', version=version, executor_class=Executor,
    config_class=Config, namespace=Collection.from_module(tasks)
)
