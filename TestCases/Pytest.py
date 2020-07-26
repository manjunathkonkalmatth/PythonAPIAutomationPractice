import pytest

from Utils.RESTServices import RESTServices


@pytest.fixture(scope='module')
def classSetUPtearDown():
    print('Module setUp')
    yield
    print('Module tearDown')


@pytest.fixture()
def testSetupTearDown():
    print('Test setUp')
    yield
    print('Test tearDown')


def test_method1(testSetupTearDown):
    print('test method1')
    rs = RESTServices()
    rs.fun()


def test_method2(testSetupTearDown):
    print('test method2')
