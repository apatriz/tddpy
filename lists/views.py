from django.shortcuts import redirect
from lists.forms import ItemForm, ExistingListItemForm
from lists.models import Item, List
from django.views.generic import FormView, CreateView
from django.views.generic.detail import SingleObjectMixin


# Create your views here.
class HomePageView(FormView):
    template_name = 'home.html'
    form_class = ItemForm


class ViewAndAddToList(CreateView, SingleObjectMixin):
    model = List
    template_name = 'list.html'
    form_class = ExistingListItemForm

    def get_form(self, form_class):
        self.object = self.get_object()
        return form_class(for_list=self.object, data=self.request.POST)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(for_list=self.object)
        return self.render_to_response(self.get_context_data(form=form))


class NewListView(CreateView):
    template_name = 'home.html'
    form_class = ItemForm

    def form_valid(self, form):
        list = List.objects.create()
        Item.objects.create(text=form.cleaned_data['text'], list=list)
        return redirect('/lists/%d/' % (list.id, ))
