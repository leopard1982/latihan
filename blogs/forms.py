from django import forms

from .models import MyBlog

class InputMyBlog(forms.ModelForm):
	class Meta:
		model = MyBlog
		fields = "__all__"

		widgets = {'tanggalbuat':forms.TextInput(attrs={'readonly':'readonly','class':'form-control'}),
			'judul':forms.TextInput(attrs={'class':'form-control'}),
			'creator':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
			'paragrafs':forms.Textarea(attrs={'class':'form-control','style':'width:100%;','wrap':'hard'})
		}