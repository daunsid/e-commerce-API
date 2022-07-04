from .. import model

def product_list(db):
    return db.query(model.Product).all()