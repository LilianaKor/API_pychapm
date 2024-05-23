
import allure
from data import get_pet_endpoints
from src.assertions import Assertions
from src.http_methods import MyRequests
from http import HTTPStatus


@allure.epic("Testing create pet")
class TestCreatePet:
    request = MyRequests()
    url = get_pet_endpoints()
    assertions = Assertions()

    def test_create_pet(self, get_test_name):
        data = """{ 
            "id": 34,
            "category": {
                "id": 47,
                "name": "string777"
        },
        "name": "doggie7",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 8,
                "name": "string"
            }
        ],
        "status": "available"              
    }"""
        response = self.request.post(url=self.url.create_pet, data=data)
        # self.assertions.assert_status_code(
        #     response=response,
        #     actual_status_code=HTTPStatus.CREATED,
        #     test_name=get_test_name
        #  )
        print(response.text)


