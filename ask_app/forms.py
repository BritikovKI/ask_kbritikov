from django import forms

class SetF(forms.Form):
    nickname=forms.CharField(max_length=10,required=False, widget=forms.TextInput(attrs={'placeholder':'nickname'}))
    login=forms.CharField(max_length=10,required=False)
    email=forms.EmailField(required=False)
    image = forms.ImageField(
        widget=forms.FileInput(
            # Mode of style of Form
            attrs={'class': 'form-control-file'}
        ),required=False)

# ,attrs={'placeholder':'{{ us.author.email }}'}
class RegF(forms.Form):
    nickname=forms.CharField(max_length=10)
    email=forms.EmailField()
    image = forms.ImageField(
        widget=forms.FileInput(
            # Mode of style of Form
            attrs={'class': 'form-control-file'}
        ))
    password=forms.CharField(widget=forms.PasswordInput())
    chPassword=forms.CharField(widget=forms.PasswordInput())

class LogF(forms.Form):
    nickname=forms.CharField(max_length=10,)
    password=forms.CharField(widget=forms.PasswordInput())

class DebF(forms.Form):
    head=forms.CharField(max_length=50)
    image = forms.ImageField(
        widget=forms.FileInput(
            # Mode of style of Form
            attrs={'class': 'form-control-file'}
        ),required=False)
    text=forms.CharField(widget = forms.Textarea(attrs={'class': 'form-control', 'rows': '20'}))
    # widget = forms.Textarea(attrs={'class': 'form-control', 'rows': '20'})
    tags=forms.CharField(widget = forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}))

class AnsF(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

class AuthF(forms.Form):
    avatar=forms.ImageField(
        widget=forms.FileInput(
            # Mode of style of Form
            attrs={'class':'form-control-file'}
        )
    )