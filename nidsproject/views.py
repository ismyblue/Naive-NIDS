from django.shortcuts import redirect,reverse


def redirectIndex(request):
    return redirect(reverse('nids:panel_index'))
