class CartSession:
    def __init__(self, session):
        self.session = session
        
        # Initialize the cart from the session or set a default
        self.cart = self.session.setdefault(
            "cart",
            {
                'items': [],
                'total_price': 0,
                'total_items': 0,
            }
        )
        
        self.clear()
        # Add a product to the cart
        self.add_product("100")
        

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

    def get_cart_items(self):
        return self.cart["items"]

    def save(self):
        self.session.modified = True
