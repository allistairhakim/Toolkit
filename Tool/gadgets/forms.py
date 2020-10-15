from django.forms import ModelForm
from .models import ToDo

class ToDoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ToDoForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['size'] = 75
    class Meta:
        model = ToDo
        fields = ['content']
