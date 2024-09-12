import requests
import pytest
import requests

BASE_URL = "https://qa-internship.avito.com/api/1"

UNIQUE_SELLER_ID = 194231

# Создание объявления
# Позитивный тест
def test_create_item_positive():
    payload = {
        "name": "Samsung Galaxy 10",
        "price": 84999,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": 10,
            "likes": 10,
            "viewCount": 10
        }
    }
    # f"{BASE_URL}/
    response = requests.post(f"https://qa-internship.avito.com/api/1/item", json=payload)
    assert response.status_code == 200
    print("Тело ответа:", response.text)
    assert 'Сохранили объявление' in response.json()['status']

# Негативный тест (пустые поля)
def test_create_item_negative_fields():
    response = requests.post(f"{BASE_URL}/item", json={})
    assert response.status_code == 500
    print("Тело ответа:", response.text)
    assert "internal error" in response.json()['message']

# Негативный тест (price string)
def test_create_item_negative_price_string():
    payload = {
        "name": "Samsung Galaxy 10",
        "price": "text",
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": 10,
            "likes": 10,
            "viewCount": 10
        }
    }
    response = requests.post(f"https://qa-internship.avito.com/api/1/item", json=payload)
    print("Тело ответа:", response.text)
    assert response.status_code == 500
    assert "internal error" in response.json()['message']

# БАГ
# Негативный тест (negative number of price)
def test_create_item_negative_price_minus():
    payload = {
        "name": "Samsung Galaxy 10",
        "price": -1,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": 10,
            "likes": 10,
            "viewCount": 10
        }
    }
    response = requests.post(f"https://qa-internship.avito.com/api/1/item", json=payload)
    print("Тело ответа:", response.text)
    assert response.status_code == 500
    assert "internal error" in response.json()['message']
# БАГ
# Негативный тест (price none)
def test_create_item_negative_price_none():
    payload = {
        "name": "Samsung Galaxy 10",
        "price": None,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": 10,
            "likes": 10,
            "viewCount": 10
        }
    }
    response = requests.post(f"https://qa-internship.avito.com/api/1/item", json=payload)
    print("Тело ответа:", response.text)
    assert response.status_code == 500
    assert "internal error" in response.json()['message']


# Негативный тест (price max) (long long before 9223372036854775807)
def test_create_item_negative_price_max():
    payload = {
        "name": "Samsung Galaxy 10",
        "price": 9223372036854775808,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": 10,
            "likes": 10,
            "viewCount": 10
        }
    }
    response = requests.post(f"https://qa-internship.avito.com/api/1/item", json=payload)
    assert response.status_code == 500
    print("Тело ответа:", response.text)
    assert "internal error" in response.json()['message']

# БАГ
# Негативный тест (пустое имя)
def test_create_item_negative_name():
    payload = {
        "name": None,
        "price": 84999,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": 10,
            "likes": 10,
            "viewCount": 10
        }
    }
    response = requests.post(f"{BASE_URL}/item", json=payload)
    print("Тело ответа:", response.text)
    assert response.status_code == 500


# Негативный тест (int имя)
def test_create_item_fake_name():
    payload = {
        "name": 123,
        "price": 84999,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": 10,
            "likes": 10,
            "viewCount": 10
        }
    }
    response = requests.post(f"{BASE_URL}/item", json=payload)
    print("Тело ответа:", response.text)
    assert response.status_code == 500
# БАГ
# Негативный тест (statistics negative contacts/likes/viewCount)
def test_create_item_stats_negative():
    payload = {
        "name": "Samsung Galaxy 10",
        "price": 84999,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": -10,
            "likes": -10,
            "viewCount": -10
        }
    }
    response = requests.post(f"{BASE_URL}/item", json=payload)
    print("Тело ответа:", response.text)
    assert response.status_code == 500

# Негативный тест (statistics negative contacts/likes/viewCount)
def test_create_item_stats_none():
    payload = {
        "name": "Samsung Galaxy 10",
        "price": 84999,
        "sellerId": UNIQUE_SELLER_ID,
        "statistics": {
            "contacts": None,
            "likes": None,
            "viewCount": None
        }
    }
    response = requests.post(f"{BASE_URL}/item", json=payload)
    print("Тело ответа:", response.text)
    assert response.status_code == 500


# Get объявление по id объявления
# Positive
def test_get_item_positive():
    item_id = '69a0e4dc-56b7-41f7-9f25-8153eb943fb3'
    response = requests.get(f"{BASE_URL}/item/{item_id}")
    print("Тело ответа:", response.text)
    assert response.status_code == 200
    item_data = response.json()
    assert isinstance(item_data, list)
    assert len(item_data) > 0

def test_get_item_negative1():
    item_id = '0010010100010010010'
    response = requests.get(f"{BASE_URL}/item/{item_id}")
    print("Тело ответа:", response.text)
    assert response.status_code == 404
    item_data = response.json()


#  Negative
def test_get_item_negative():
    item_id = "NotRealId"
    response = requests.get(f"{BASE_URL}/item/{item_id}")
    print("Тело ответа:", response.text)
    assert response.status_code == 404

# Get на все объявления по sellerID
# Positive
def test_get_items_by_sellerid_positive():
    response = requests.get(f"{BASE_URL}/{UNIQUE_SELLER_ID}/item")
    print("Тело ответа:", response.text)
    assert response.status_code == 200
    items = response.json()
    assert isinstance(items, list)
    # print(items)

#БАГ
# Negative
def test_get_items_by_sellerid_negative():
    nonexistent_seller_id = "FakeData"
    response = requests.get(f"{BASE_URL}/{nonexistent_seller_id}/item")
    print("Тело ответа:", response.text)
    assert response.status_code == 404
