from django import forms
from proteinWeb.models import Document, PDBName


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ("description", 'document',)


class PDBNameForm(forms.Form):
    pdbName = forms.CharField()

    class Meta:
        model = PDBName
        fields = ('name',)
