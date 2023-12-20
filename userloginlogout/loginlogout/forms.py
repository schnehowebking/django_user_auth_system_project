from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']



class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = '__all__'



class UserChangePasswordwithoutForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserChangePasswordwithoutForm, self).__init__(*args, **kwargs)
        

    class Meta:
        model = User
        fields = ['password1', 'password2']