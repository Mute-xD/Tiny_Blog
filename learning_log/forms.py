from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text', 'isPublic']
        labels = {'text': '', 'isPublic': '设为公开，其他用户登陆后可以看到这个话题'}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'isPublic']
        labels = {'text': '', 'isPublic': '设为公开，其他用户登陆后可以看到这个内容'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
