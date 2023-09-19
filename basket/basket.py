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
    
    def add(self, product):
        product_id = product.id

        if product.id not in self.basket:
            self.basket[product_id] = {'price': str(product.price)}
        
        self.session.modified = True
            