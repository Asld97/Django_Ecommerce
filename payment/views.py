from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from basket.basket import Basket
import stripe

# Create your views here.
@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.','')
    total = int(total)

    print(total)
    stripe.api_key = 'sk_test_51NzKZwLxGQ0N3mNagLW3BGcrBkEJUimfJH2Ufaf9465fBU50WYebW4hNXroCnfr7FGNB4PvplkBaiu3p2QE6H29Z00d50Lg48j'
    intent = stripe.PaymentIntent.create(        
        amount = total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )


    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})

