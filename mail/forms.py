from django.conf import settings
from django import forms
from django.core.mail import send_mail


class UserForm(forms.Form):
    username=forms.CharField(max_length=120)
    email=forms.EmailField()
    inquiry=forms.CharField()
    message=forms.CharField(widget=forms.Textarea)

  # recieve and clean data
    def get_info(self):    
        # cleaned data
        cl_data=super().clean()

        name = cl_data.get('username').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('inquiry')
         
        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):
        subject,msg =self.get_info()
        
        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )