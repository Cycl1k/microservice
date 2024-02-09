import unittest
import requests


class TestFlaskApiUsingRequests(unittest.TestCase):
    def test_login1(self):
        response = requests.get('http://127.0.0.1:8000/greet/hhh')
        self.assertEqual(response.json(),'Привет, hhh от Python!')

    def test_login2(self):
        response = requests.get('http://127.0.0.1:8000/greet/Marya')
        self.assertEqual(response.json(),'Привет, Marya от Python!')

    def test_login3(self):
        response = requests.get('http://127.0.0.1:8000/greet/0001')
        self.assertEqual(response.json(),'Привет, 0001 от Python!')
    
    def test_login4(self):
        response = requests.get('http://127.0.0.1:8000/greet/----')
        self.assertEqual(response.json(),'Привет, ---- от Python!')

    #Для Go сервиса
    def test_login5(self):
        response = requests.get('http://127.0.0.1:8080/greet/gg')
        self.assertEqual(response.json(),'Привет от Go!')

    def test_login6(self):
        response = requests.get('http://127.0.0.1:8080/greet/Marya')
        self.assertEqual(response.json(),'Привет от Go!')
    def test_login7(self):
        response = requests.get('http://127.0.0.1:8080/greet/----')
        self.assertEqual(response.json(),'Привет от Go!')

    

if __name__ == "__main__":
    unittest.main()