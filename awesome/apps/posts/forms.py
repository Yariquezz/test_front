from django import forms
from .models import Post, Category


choice_list = [
    ("music", "music"),
    ("sports", "sports"),
    ("news", "news"),
]


class CreatePostForm(forms.ModelForm):

    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(attrs={
            "class": "form-control",
        })
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
        })
    )

    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "author",
            "status",
            "category",
            "image_1",
            "image_2",
            "image_3",
        )
        widget = {
            "author": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "categoty": forms.Select(choices=choice_list, attrs={"class": "form-select"}),
        }


class EditPostForm(forms.ModelForm):
    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(attrs={
            "class": "form-control",
        })
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
        })
    )
    category = forms.Form(
        forms.ChoiceField(
            choices=choice_list,
            widget=forms.Select(
                attrs={
                    "class": "form-select"
                }
            )
        )
    )

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "category",
            "image_1",
            "image_2",
            "image_3",
        ]
