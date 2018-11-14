from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(max_length=100,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'aria-describedby': 'add-btn'}))
    comment = forms.CharField(max_length=280,
                              widget=forms.Textarea())

