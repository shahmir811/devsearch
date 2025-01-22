from django import forms

from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        # fields = '__all__'
        fields = ['title', 'feature_image','description', 'demo_link', 'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        # Add input css class to every field
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})



