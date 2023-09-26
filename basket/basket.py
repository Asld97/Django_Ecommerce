from store.models import Product
from decimal import Decimal

class Basket():
    """
    A base Basket class, providing some default behaviours that can be inherited or overrided as necesseary
    """

    def __init__(self, request):  # Run on initializing class -> create session when creating basket
        self.session = request.session 
        basket = self.session.get('skey')
        if 'skey' not in self.session:
            basket = self.session['skey'] = {}
        
        self.basket = basket
    
    def add(self, product, qty):
        product_id = product.id

        if product.id not in self.basket:
            self.basket[product_id] = {'price': str(product.price), 'qty': int(qty)}
        
        self.save()
    
    def __iter__(self):
        """
        Collect the product_id in the session data to query database and return products
        """
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item
        
    def __len__(self):
        """
        Get the basket data and count the qty of items
        """

        return sum(item['qty'] for item in self.basket.values())
        
    def get_total_price(self):
        return sum(float(item['price']) * item['qty'] for item in self.basket.values())
    
    def delete(self, product):
        """
        Delete item from session data
        """
        product_id = str(product)
        if product_id in self.basket:
            del self.basket[product_id]
        
        self.save()

        

    def save(self):
        self.session.modified = True