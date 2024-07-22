
import allure
from data import get_pet_endpoints
from src import CreatePetShem
from src.assertions import Assertions
from src.http_methods import MyRequests
from http import HTTPStatus

from src.validator import Validator
import json


@allure.epic("Testing create pet")
class TestCreatePet:
    request = MyRequests()
    url = get_pet_endpoints()
    assertions = Assertions()
    validator = Validator()

    def test_create_pet(self, get_test_name):
        data = """{ 
            "id": 35,
            "category": {
                "id": 0,
                "name": "string777"
            },
            "name": "doggie71",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 888,
                    "name": "string"
                }
            ],
            "status": "available"              
        }"""
        response = self.request.post(url=self.url.create_pet, data=data)
        print(response.text)
        self.assertions.assert_status_code(
            response=response,
            actual_status_code=HTTPStatus.OK,
            test_name=get_test_name
         )
        self.validator.validate_response(response=response, model=CreatePetShem.create_pet)





        #  Validate the status code
        # self.assertions.assert_status_code(
        #     response=response,
        #     actual_status_code=HTTPStatus.CREATED,  # Ensure this is the expected status code
        #     test_name=get_test_name
        # )


