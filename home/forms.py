from django import forms

class RegForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Name","id":"form_name"}))
    number = forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter Number","id":"form_name"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password","id":"form_name"}))

class LoginForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Name","id":"form_name"}))
    #number = forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter Number","id":"form_name"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password","id":"form_name"}))

class NotesForm(forms.Form):
    contents = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Write Note here.","id":"form_name"}))