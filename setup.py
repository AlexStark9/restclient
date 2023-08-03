from distutils.core import setup
REQUIRES = [
    'requests',
    'structlog',
    'curlify',
    'allure-pytest'
]

setup(
    name='restclient',
    version='0.0.1',
    packages=['rest_client'],
    url='https://github.com/AlexStark9/restclient.git',
    license='MIT',
    author='Alex Stark',
    author_email='-',
    install_requires=REQUIRES,
    description='restclient with allure and loger'
)
