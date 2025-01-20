from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from django.core.exceptions import ValidationError
import re


class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'

		self.fields['username'].label = 'Логин'
		self.fields['email'].label = 'Email'
		self.fields['password1'].label = 'Пароль'
		self.fields['password1'].help_text = 'Минимум 8 символов, должен содержать цифры и заглавные буквы.'
		self.fields['password2'].label = 'Подтверждение пароля'
		self.fields['password2'].help_text = 'Повторите пароль для подтверждения.'

		self.fields['username'].help_text = 'Минимум 3 символа. Только буквы, цифры и знак подчеркивания.'

		self.fields['username'].widget.attrs.update(
			{
				'class': 'form-control',
				'placeholder': 'Введите логин'
			}
		)

		self.helper.layout = Layout(
			Row(
				Column('username', css_class='form-group col-md-6 mb-3'),
				Column('email', css_class='form-group col-md-6 mb-3'),
				css_class='form-row'
			),
			Row(
				Column('password1', css_class='form-group col-md-6 mb-3'),
				Column('password2', css_class='form-group col-md-6 mb-3'),
				css_class='form-row'
			),
			Submit('submit', 'Зарегистрироваться', css_class='btn btn-primary bg-gradient')
		)

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def clean_username(self):
		username = self.cleaned_data['username']
		if len(username) < 3:
			raise ValidationError('Имя пользователя должно содержать не менее 3 символов')
		if not re.match(r'^[a-zA-Z0-9_]+$', username):
			raise ValidationError('Имя пользователя может содержать только буквы, цифры и знак подчеркивания')
		if User.objects.filter(username=username).exists():
			raise ValidationError('Пользователь с таким именем уже существует')
		return username

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			raise ValidationError('Пользователь с таким email уже существует')
		return email

	def clean_password1(self):
		password1 = self.cleaned_data['password1']
		if len(password1) < 8:
			raise ValidationError('Пароль должен содержать не менее 8 символов')
		if not any(char.isdigit() for char in password1):
			raise ValidationError('Пароль должен содержать хотя бы одну цифру')
		if not any(char.isupper() for char in password1):
			raise ValidationError('Пароль должен содержать хотя бы одну заглавную букву')
		return password1

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise ValidationError('Пароли не совпадают')
		if not password2:
			raise ValidationError('Поле пароля не может быть пустым')
		return password2
