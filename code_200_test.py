# Владислав Земляков, 10-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request

def positive_assert_code_200():
    response = sender_stand_request.post_new_order()
    track_number = response.json()["track"]
    order_response = sender_stand_request.receive_an_order(track_number)
    assert order_response.status_code == 200

def test_code_200():
    positive_assert_code_200()