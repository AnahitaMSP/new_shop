from django.shortcuts import get_object_or_404

from shop.models import ProductModel,ProductStatusType


class CartSession:

    total_payment_price = 0
    def __init__(self, session):
        self.session = session
        self.cart = self.session.setdefault(
            "cart",
            {
                'items': [],
                'total_price': 0,
                'total_items': 0,
            }
        )

        # self.clear()
        self.save()

    def add_product(self, product_id):
        # Check if the product already exists in the cart
        for item in self.cart['items']:
            if product_id == item['product_id']:
                item['quantity'] += 1
                break
        else:
            # If the product does not exist, create a new item
            new_item = {
                "product_id": product_id, 
                "quantity": 1, 
            }
            self.cart['items'].append(new_item)
        self.save()

    def clear(self):
        self.cart = self.session['cart']={
            
                'items': [],
                'total_price': 0,
                'total_items': 0,
            }
        
        self.save()

    def get_cart_dict(self):
        return self.cart

    def get_cart_items(self):
        cart_items = self.cart['items']
        self.total_payment_price = 0
        for item in cart_items:
            try:
                product_obj = ProductModel.objects.get(id=item['product_id'], status=ProductStatusType.publish.value)
                item['product_obj'] = product_obj.to_dict()  # Use the new method

                total_price = int(item["quantity"]) * product_obj.get_price()
                item['total_price'] = total_price
                self.total_payment_price += total_price
            except ProductModel.DoesNotExist:
                print(f"Product with ID {item['product_id']} does not exist or is not published.")
                continue

        return cart_items

    def get_total_payment_amount(self):
        return self.total_payment_price
 
    def get_total_quantity(self):

        total_quantity = len(self.cart['items'])
        return total_quantity

    def update_product_quantity(self,product_id,quantity):
        for item in self.cart['items']:
            if product_id == item['product_id']:
                item['quantity'] = quantity
                break

        self.save()

    def remove_product(self,product_id):
        for item in self.cart['items']:
            if product_id == item['product_id']:
                self.cart['items'].remove(item)
                break
        self.save()


    def save(self):
        self.session.modified = True
