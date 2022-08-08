from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout, Submit, Div
from crispy_forms.bootstrap import PrependedText
        
class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_contact-form'
        self.helper.form_class = 'contact-form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Div(
                Div(
                PrependedText('firstName', text='', placeholder='First Name'),
                css_class = 'firstname'
                ),
                Div(
                PrependedText('lastName', text='', placeholder='Last Name'),
                css_class = 'lastname'
                ),
                css_id = 'contact-name'
            ),
            Div(
                Div(
                PrependedText('emailAddress', text='', placeholder='Email Address'),
                css_class = 'emailaddress-form'
                ),
                Div(
                PrependedText('phoneNumber', text='', placeholder='Phone Number'),
                css_class = 'phonenumber-form'
                ),
                css_id = 'contact-contact'
            ),
            Div(
                Div(
                PrependedText('address1', text='', placeholder='Address (include Apartment Number If applicable)'),
                css_class = 'address-form'
                ),
                Div(
                PrependedText('city', text='', placeholder='City'),
                css_class = 'city-form'
                ),
                Div(
                PrependedText('state', text='', placeholder='State'),
                css_class = 'state-form'
                ),
                Div(
                PrependedText('zipCode', text='', placeholder='Zip'),
                css_class = 'zipcode-form'
                ),
                css_id = 'contact-address'
            ),
            PrependedText('message', text='', placeholder='Please list any information about your Area Rugs, such as quantity, approximate size, and material'),
            PrependedText('serviceDate', text='', placeholder='When would you like us to pick up your Area Rug(s)?'),
        )


    firstName = forms.CharField(
        widget=forms.TextInput(attrs={'style':'width: 25rem'}),
        max_length=50,
    )
    lastName = forms.CharField(
        widget=forms.TextInput(attrs={'style':'width: 25rem'}),
        max_length=50, 
    )
    emailAddress = forms.EmailField(
        widget=forms.TextInput(attrs={'style':'width: 25rem'}),
        max_length=50, 
    )
    phoneNumber = forms.CharField(
        widget=forms.TextInput(attrs={'style':'width: 25rem'}),
        max_length=20,
    )
    address1 = forms.CharField(
        widget=forms.TextInput(attrs={'style':'width: 25rem'}),
        max_length=225, 
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={'style':'width: 15rem'}),
        max_length=225,
    )
    state = forms.CharField(
        widget=forms.TextInput(attrs={'style':'width: 4.5rem'}),
    )
    zipCode = forms.CharField(
        widget=forms.TextInput(attrs={'style':'width: 5rem'}),
        max_length=5,
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={ 'class': 'message-widget-form'}),
        label="Please list any information about your Area Rugs, such as quantity, approximate size, and material",
    )
    serviceDate = forms.CharField(
        widget=forms.TextInput(attrs={'style':'max-width: 50.5rem'}),
        max_length=50,
        label="When would you like us to pick up your Area Rug(s)?",
    )