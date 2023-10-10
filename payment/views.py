from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
import stripe
import json
from basket.basket import Basket
from orders.views import payment_confirmation

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

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        
        print(e)
        return HttpResponse(status=400)
    
    
    # Handle the event
    if event.type == 'payment_intent.succeeded':
        
        payment_confirmation(event.data.object.client_secret)

    else:
        print('Unhandled event type {}'.format(event.type))
    
    return HttpResponse(status=200)

def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'payment/orderplaced.html')