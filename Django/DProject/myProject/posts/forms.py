from django import forms


from .models import post


class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = [
            "title",
            "slug",
            "image",
            "author",
            "body",
            "publish",
            "status",
            "is_active"
        ]

class NameForm(forms.Form):
    # blank args allow user to enter empty value
    # null to accept null values in DB
    your_name = forms.CharField(label='Name',
                                required=False,
                                max_length=100)
    active = forms.BooleanField(required=True)