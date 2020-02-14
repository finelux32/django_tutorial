from django import forms


class BoardWriteForm(forms.Form):
    subject = forms.CharField(max_length=40, label="제목", error_messages={'required': '제목을 입력하세요'})
    contents = forms.CharField(label="내용", error_messages={'required': '내용를 입력하세요!!'})

    def clean(self):
        cleaned_data = super().clean()
        # TODO Validation Logic

        # assignment
        self.subject = cleaned_data.get('subject')
        self.contents = cleaned_data.get('contents')

