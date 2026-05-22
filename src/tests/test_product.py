from daos.product_dao import ProductDAO
from models.product import Product

dao = ProductDAO()

def test_product_select():
    product_list = dao.select_all()
    assert len(product_list) >= 2


def test_product_insert():
    product = Product(None, 'OSRS', 'JAGEX', 100)
    assigned_id = dao.insert(product)
    product_list = dao.select_all()
    names = [u.name for u in product_list]
    assert product.name in names

    # cleanup
    dao.delete(assigned_id)

def test_product_update():
    product = Product(None, 'Ziao', 'MIA', 100)
    assigned_id = dao.insert(product)

    corrected_brand = 'Mia-lite'
    product.id = assigned_id
    product.brand = corrected_brand
    dao.update(product)

    product_list = dao.select_all()
    brands = [u.brand for u in product_list]
    assert corrected_brand in brands

    # cleanup
    dao.delete(assigned_id)

def test_product_delete():
    product = Product(None, 'Big', 'Binotte', 420)
    assigned_id = dao.insert(product)
    dao.delete(assigned_id)

    new_dao = ProductDAO()
    product_list = new_dao.select_all()
    brands = [u.brand for u in product_list]
    assert product.brand not in brands