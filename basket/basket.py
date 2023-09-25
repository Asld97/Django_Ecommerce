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
        
        self.session.modified = True
    
    def __len__(self):
        """
        Get the basket data and count the qty of items"""

        return sum(item['qty'] for item in self.basket.values())
            