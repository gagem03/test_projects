import pytest
from login_form import LoginForm


#a fresh form for each test
@pytest.fixture
def form():
    return LoginForm()

#setup the paramatrize test data for the email validation
@pytest.mark.parametrize("email", [
    "user@example.com",
    "balls@example.com",
    "NotAi@ai.com",
    "joebiden@thewhitehouse.com",
    "boejiden@theblackhouse.com",
    "yarrmematey@piratebay.com",
    "santaclaus@thenorthpole.org",
    "petergriffin@spoonerstreet.org",
    "teacher@teacherland.edu",
    "test@testing.com",
    "thepythonman@python.com",
    "notch@minecraft.net",
    "bartsimpson@bartsimpson.bart",
    "themoneyman@dollarbill.com",
    "gangster@crimedoer.com",
    "imhungry@food.com",
    "dev_team@startup.tech"
])
# positive test case
def test_valid_email(form, email):
    assert LoginForm.validate_email(form, email) is True

@pytest.mark.parametrize("invalid_email", [
    "asjfjaslkfjkasfj.com",
    "####################",
    "-___-__-",
    "233-45",
    "user.domain"
])

# negative test case
def test_invalid_email(form, invalid_email):
    assert LoginForm.validate_email(form, invalid_email) is False

# setup the tests for password validation
@pytest.mark.parametrize("password", [
    "Password123",
    "SecurePass456",
    "MyStrongPass789",
    "ValidPass1",
    "AnotherPass2",
    "UpperCase3"
])

# test the validation
def test_valid_password(form, password):
    assert LoginForm.validate_password(form, password) is True