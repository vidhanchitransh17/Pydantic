# Pydantic v2 Example: Data Validation, Serialization & Computed Fields

This project demonstrates how to use **Pydantic v2** features like:

- `Field` function for metadata and validation  
- `Annotated` types  
- **Field Validators** (`@field_validator`)  
- **Model Validators** (`@model_validator`)  
- **Computed Fields** (`@computed_field`)  
- Nested models  
- Serialization with `model_dump` & `model_dump_json`  

---

## 📂 Code Overview

```python
from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator, model_validator, computed_field
from typing import Annotated

# ✅ Nested Model for Address
class address(BaseModel):
    city: Annotated[str, Field(title="Name of city")]
    state: Annotated[str, Field(title="Name of state")]
    pincode: Annotated[int, Field(title="Pincode of address")]

# ✅ Main Model for Engineer
class engineer(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Name of Person")]
    age: Annotated[int, Field(gt=4, title="Age of person")]
    email: Annotated[EmailStr, Field(title="Email of the user")]
    url: Annotated[AnyUrl, Field(title="Linked Profile URL")]
    address: address

    # Field validator for email domain
    @field_validator("email")
    @classmethod
    def email_validate(cls, value):
        valid = ["pwc.com", "gmail.com"]
        domain = value.split("@")[-1]
        if domain not in valid:
            raise ValueError("incorrect value for email")
        return value

    # Field validator (after) for transforming name
    @field_validator("name", mode="after")
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    # Model-level validation
    @model_validator(mode="after")
    def validate_person(cls, model):
        if model.age < 20 and model.name == "VIDHAN":
            raise ValueError("Name should not be vidhan")
        return model

    # Computed field
    @computed_field
    @property
    def sign(self) -> str:
        return f"{self.name}{self.age}"
