import smtplib
import pytest

@pytest.fixture(scope="module")
def smtp_connection(request):
    server = getattr(request.module, "smtpserver", "smtp.gmail.com")
    smtp_connection = smtplib.SMTP(server, 587, timeout=5)
    yield smtp_connection
    print(f"finalizing {smtp_connection} ({server})")
    smtp_connection.close()
