from typing import List

import pytest
from tests.factories import product_data
from fastapi import status

async def test_controller_create_should_return_success(client, products_url):
    response = await client.post(products_url, json=product_data(name="iPhone 14 Pro Max"))

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json().get("name") == "iPhone 14 Pro Max"

async def test_controller_create_should_return_422(client, products_url):
    response = await client.post(products_url, json={})

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

async def test_controller_get_should_return_success(client, product_inserted, products_url):
    response = await client.get(f"{products_url}/{product_inserted.id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("name") == product_inserted.name

async def test_controller_get_should_return_not_found(client, products_url):
    response = await client.get(f"{products_url}/1e4f214e-85f7-461a-89d0-a751a32e3bb9")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json().get("detail") == "Product not found with filter: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"

@pytest.mark.usefixtures("products_inserted")
async def test_controller_query_should_return_success(client, products_url):
    response = await client.get(products_url)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), List)
    assert len(response.json()) > 1

async def test_controller_update_should_return_success(client, product_inserted, products_url):
    response = await client.patch(f"{products_url}/{product_inserted.id}", json={"price": 7500})

    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("price") == 7500

async def test_controller_update_should_return_not_found(client, products_url):
    response = await client.patch(f"{products_url}/1e4f214e-85f7-461a-89d0-a751a32e3bb9", json={"price": 7500})

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json().get("detail") == "Product not found with filter: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"

async def test_controller_delete_should_return_success(client, product_inserted, products_url):
    response = await client.delete(f"{products_url}/{product_inserted.id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT

async def test_controller_delete_should_return_not_found(client, products_url):
    response = await client.delete(f"{products_url}/1e4f214e-85f7-461a-89d0-a751a32e3bb9")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json().get("detail") == "Product not found with filter: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"
