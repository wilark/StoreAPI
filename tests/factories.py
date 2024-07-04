from datetime import datetime
from decimal import Decimal
from uuid import UUID, uuid4

def product_data(name: str = "iPhone 14 Pro Max"):
    return {
        "id": uuid4(),
        "name": name,
        "quantity": 10,
        "price": Decimal("7500.00"),
        "status": True,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
