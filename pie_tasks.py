from pie import *


@task
def setup():
    createVenvs()
    updatePackages()


@task
def createVenvs():
    venv(r'venvs\test').create('--system-site-packages')


@task
def updatePackages():
    with venv(r'venvs\test'):
        pip(r'install -U pip')
        pip(r'install -U -r requirements.test.txt')


@task
def test():
    with venv(r'venvs\test'):
        cmd(r'python -m pytest -s tests')


@task
def register():
    cmd(r'python setup.py register')


@task
def build(upload=False):
    cmd(r'python setup.py clean --all bdist_wheel{}'.format(' upload' if upload else ''))
