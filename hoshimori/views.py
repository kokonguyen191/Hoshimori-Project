# Create your views here.
from copy import copy

from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render
from magi.utils import globalContext as web_globalContext, ajaxContext

from hoshimori.magicollections import CardCollection
from hoshimori.models import *
from hoshimori.utils import item_view, filterCards


def globalContext(request):
    context = web_globalContext(request)
    context['something'] = 'something'
    return context


def cardstat(request, card):
    context = ajaxContext(request)
    context['card'] = get_object_or_404(Card, pk=card)
    return render(request, 'include/cards-stats.html', context)


def addcard(request, card):
    if request.method != "POST":
        raise PermissionDenied()
    collection = 'collection' in request.GET
    queryset = Card
    if not collection:
        # Note: calling filterCards will add extra info need to display the card
        queryset = filterCards(Card.objects.all(), {}, request)
    card = get_object_or_404(queryset, pk=card)
    account = get_object_or_404(Account, pk=request.POST.get('account', None), owner=request.user)
    OwnedCard.objects.create(card=card, account=account)
    if not collection:
        card.total_owned += 1
    if collection:
        return cardcollection(request, card.id)
    else:
        context = web_globalContext(request)
        return item_view(request, context, 'card', CardCollection, pk=card.id, item=card, ajax=True)


def cardcollection(request, card):
    context = web_globalContext(request)
    collection = copy(CardCollection)
    request.GET = request.GET.copy()
    request.GET['collection'] = True
    collection.ItemView.template = '../include/cards-collection'
    return item_view(request, context, 'card', collection, pk=card, ajax=True)


def account_about(request, account):
    context = ajaxContext(request)
    context['account'] = get_object_or_404(Account.objects.select_related('starter'), pk=account)
    return render(request, 'ajax/account_about.html', context)
