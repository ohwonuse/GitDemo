import pytest


@pytest.mark.smoke
def test_fisrtProgrm(setup):
    print('Hello')

@pytest.mark.xfail
def test_secondGreetCreditCard():
    print('Good Morning')

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])