import pytest
from base.Base import Base

@pytest.fixture #(scope='session')
def tbase(request):
    fixture = Base()
    # Doesn't work this finalazer, need to check later
    # request.addfinalazer(fixture.close_browser)
    return fixture