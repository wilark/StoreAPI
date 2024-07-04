from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from decimal import Decimal
from bson import Decimal128
from pydantic import AfterValidator

class ProductModel(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias="_id")
    name: str
    quantity: int
    price: Decimal
    status: bool
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {
            Decimal128: lambda v: Decimal128(str(v)),
        }

    @AfterValidator
    def validate_decimal128(cls, v):
        if isinstance(v, Decimal128):
            return Decimal(v.to_decimal())
        return v
