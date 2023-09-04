from django import forms
from django.core import validators
# from app_two.models import User
from django.contrib.auth.models import User
from app_two.models import UserProfileInfo



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')


# class InputUser(forms.ModelForm):
#     # first_name = forms.CharField(max_length=264)
#     # last_name = forms.CharField(max_length=264)
#     # email = forms.EmailField(label = "Email")
#     class Meta:
#         model = User
#         fields = "__all__"
#
# def check_for_a(value):
#     if value[0] != "a":
#         raise forms.ValidationError("your name shuld start from A!")
#
# class FormName(forms.Form):
#     name = forms.CharField(validators = [check_for_a])
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label='Enter your email again:')
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required=False, widget = forms.HiddenInput,
#             validators =[validators.MaxLengthValidator(0)] ) #testing for bot
#     #botcatcher = forms.CharField(required=False, widget = forms.HiddenInput)
#
#     # def clean_botcacher(self):
#     #     botcatcher = self.cleaned_data['botcatcher']
#     #     if len(botcatcher) > 0:
#     #         raise forms.ValidationError("GOTCHA BOT!")
#     #     return botcatcher
#
#     def clean(self):
#         all_clean_data = super().clean()
#         email = all_clean_data['email']
#         vmail = all_clean_data['verify_email']
#
#         if email != vmail:
#             raise forms.ValidationError("MAKE SURE EMAILS MATCH!")
