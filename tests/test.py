import os
from unittest import TestCase
from salt_client.client import SaltClient

test_cluster_url = os.getenv("SALT_MASTER_URL", "http://localhost:8000")
test_cluster_user = os.getenv("SALT_MASTER_USER", "vscode")
test_cluster_user_pass = os.getenv("SALT_MASTER_USER_PASS", "123456$")

class TestSaltClient(TestCase):

    def test_run_command(self):
        client = SaltClient(test_cluster_url,
                            salt_username=test_cluster_user,
                            salt_password=test_cluster_user_pass)
        token = client.login()
        print(token)
        response = client.run_command("*", "test.ping")
        print(response)

    def test_run_pgrep(self):
        client = SaltClient(test_cluster_url,
                            salt_username=test_cluster_user,
                            salt_password=test_cluster_user_pass)
        token = client.login()
        print(token)
        response = client.run_command("*", "ps.psaux", "salt-minion")
        print(response)

