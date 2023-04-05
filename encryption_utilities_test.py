#Unit tests for password encryption utilities
import unittest
from encryption_utilities import passwordEncrypt

class TestEncryptionMethods(unittest.TestCase):
    def test_encrypt_password(self):
        encryptedPassword = passwordEncrypt("XqffoZeo", 16)
        assert encryptedPassword == "NgvvePue"
    def test_decrypt_password(self):
        encryptedPassword = passwordEncrypt("NgvvePue", -16)
        assert encryptedPassword == "XqffoZeo"
