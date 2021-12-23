from django import forms

from blog.models import Article, Tag


class ArticleForm(forms.ModelForm):

    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)

    class Meta:
        model = Article
        fields = (
            'title',
            'content',
            'image',
            'tags',
        )