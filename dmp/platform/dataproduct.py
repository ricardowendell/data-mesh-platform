from dataclasses import dataclass


@dataclass
class DataProductSpecification:
    """Class for defining attributes for a Data Product"""

    name: str
    domain: str
    owner: str


def create(product_spec):
    print(f"Creating data product {product_spec.name}...")
    scaffold(product_spec)


def scaffold(product_spec):
    print("TODO: create data product repository")
    print("TODO: create data product blob storage")
