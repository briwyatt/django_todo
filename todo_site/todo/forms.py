from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(max_length=100,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'aria-describedby': 'add-btn'}))
