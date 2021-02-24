import pytest

@pytest.fixture(scope= 'class')
def setup():
    print('I will be executing first')
    yield
    print('I will be executed last')

@pytest.fixture()
def dataLoad():
    print('user profile data is being created')
    return ['Rahul', 'Shetty', 'rehulshettyacademy.com']

@pytest.fixture(params= [('chrome', 'Rahul', 'shetty'), ('firefox', 'shetty'), ('IE', 'SS')])
def crossBrowser(request):
    return request.param