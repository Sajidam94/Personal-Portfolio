from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'name',
        'id': 'name',
        'type': 'text',
        'class': 'form-control b-box',
        'placeholder': 'Your Name*',
        'required': True
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'email',
        'id': 'email',
        'type': 'email',
        'class': 'form-control b-box',
        'placeholder': 'Your Email*',
        'required': True
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'subject',
        'type': 'text',
        'class': 'form-control b-box',
        'placeholder': 'Your Subject..'
    }))
    comments = forms.CharField(widget=forms.Textarea(attrs={
        'name': 'comments',
        'id': 'comments',
        'rows': '4',
        'class': 'form-control b-box',
        'placeholder': 'Your message...'
    }))
