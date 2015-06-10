from django.contrib.auth.models import User
from django import forms
from .models import newlist, newlistitem
from crispy_forms.bootstrap import AppendedText, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from crispy_forms.layout import Field
from crispy_forms.bootstrap import AppendedText, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from crispy_forms.layout import Field
from django.contrib.auth.models import User

class NewListForm(forms.ModelForm):

	class Meta:
		exclude = ["user"]
		model = newlist
		widgets = {
			'list_name': forms.TextInput(attrs={'class': 'float',  'placeholder': 'ADD NEW FAVORITR LIST'}),
		}

	def __init__(self, *args, **kwargs):
		super(NewListForm, self).__init__(*args, **kwargs)
		self.fields['list_name'].label = False
		self.fields['list_name'].required = False
		self.fields['picture'].label = False
		for field in self.fields.values():
			field.error_messages = {'required':''.format(
				fieldname=field.label)}


class UserForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter User Name', 'class': 'regform'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter User Password', 'class': 'regform'}))

	def __init__(self, *args, **kwargs):
			super(UserForm, self).__init__(*args, **kwargs)
			self.fields['username'].label = False
			self.fields['password'].label = False
			self.helper = FormHelper()
			self.helper.layout = Layout(
				'username',
				'password',
				ButtonHolder(
					Submit('Submit', 'Register', css_class='btn-primary' , css_id = "floater")
				),    
			)
	class Meta:
		model = User
		fields = ('username', 'password', )







class NewListItemForm(forms.ModelForm):

	class Meta:
		model = newlistitem
		fields = ["list_item"]
		widgets = {
			'list_item': forms.TextInput(attrs={'class': 'form-control', 'align':'center',  'placeholder': 'Add Item To List'}),
		}

	def __init__(self, *args, **kwargs):
		super(NewListItemForm, self).__init__(*args, **kwargs)
		self.fields['list_item'].label = False
		self.fields['list_item'].required = True

		for field in self.fields.values():
			field.error_messages = {'required':''.format(
				fieldname=field.label)}
