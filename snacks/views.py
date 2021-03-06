from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse

from .models import Snack


class SnackListView(ListView):
    template_name = 'snack-list.html'
    model = Snack


class SnackDetailView(DetailView):
    template_name = 'snack-detail.html'
    model = Snack
    fields = ['name', 'description', 'purchaser']


class SnackCreateView(CreateView):
    template_name = 'snack-create.html'
    model = Snack
    fields = ['name', 'description', 'purchaser']
    success_url = reverse_lazy('snack_list')


class SnackDeleteView(DeleteView):
    template_name = 'snack-delete.html'
    model = Snack
    success_url = reverse_lazy('snack_list')


class SnackUpdateView(UpdateView):
    template_name = 'snack-update.html'
    model = Snack
    fields = ['name', 'description', 'purchaser']

    def get_success_url(self):
        return reverse('snack_detail', kwargs={'pk': self.kwargs['pk']})