from django import forms
from .models import Form
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit,Fieldset,Div,Field,HTML
from crispy_forms.bootstrap import FormActions,TabHolder,Tab,AppendedText
from django.shortcuts import get_object_or_404
class QueryForm(forms.ModelForm):

    class Meta:
        model = Form
        fields = ('name', 'email', 'query', 'institute')
    def __init__(self, *args, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'query-form'
        self.helper.layout = Layout(
            
       
           
           
            
             Div(

             Div( 
             Div(
            Field('name',wrapper_class='input--style-4'),
             css_class='input-group'),
             css_class='col-2'),
           
            Div( 
             Div(
            Field('email',wrapper_class='input--style-4'),
             css_class='input-group'),
             css_class='col-2'),

             css_class='row row-space'
             ),

            #institute
             Div(
            Field('institute',wrapper_class='form-group col-md-12'),
             css_class='row row-space'
             ),

           #Query
           Div(
            Field('query',wrapper_class='form-group col-md-12'),
             css_class='row row-space'
             ),
            # Field('query',wrapper_class='form-group col-md-12'),
           
             
            
         Div(
            FormActions(
            Div(Div(Submit('save', 'SEND',css_class="btn-success"),style='display: inline-block;margin-top:50px;padding:10px;margin-left:10px;'),style='text-align: center'),
              
            )
           ,style="margin: 12px;"),
           
        
        )

class ReplyForm(forms.ModelForm):

    class Meta:
        model = Form
        fields = ('replied_by', 'reply', 'secret_code')
    def __init__(self, *args, **kwargs):
        super(ReplyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'reply-form'
        self.helper.layout = Layout(
            
       
           
           
            
             Div(

             Div( 
             Div(
            Field('replied_by',wrapper_class='input--style-4'),
             css_class='input-group'),
             css_class='col-2'),
           
            Div( 
             Div(
            Field('secret_code',wrapper_class='input--style-4'),
             css_class='input-group'),
             css_class='col-2'),

             css_class='row row-space'
             ),

           
           #reply
           Div(
            Field('reply',wrapper_class='form-group col-md-12'),
             css_class='row row-space'
             ),
           
           
             
            
         Div(
            FormActions(
            Div(Div(Submit('save', 'REPLY',css_class="btn-success"),style='display: inline-block;margin-top:50px;padding:10px;margin-left:10px;'),style='text-align: center'),
              
            )
           ,style="margin: 12px;"),
           
        
        )

    def clean_secret_code(self):
        code = self.cleaned_data.get('secret_code')
        current_question = get_object_or_404(Form, pk=self.instance.pk)
        secret_code = current_question.secret_code_value
        if code!=secret_code:
            raise forms.ValidationError("Invalid Secret Code")
        return code

class DeleteForm(forms.ModelForm):

    class Meta:
        model = Form
        fields = ('secret_code',)
    def __init__(self, *args, **kwargs):
        super(DeleteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'reply-form'
        self.helper.layout = Layout(
             Div(
       
           
           
            Div(Div(HTML('<p style="color: red;"><strong>Fill the following form to delete the selected query</strong></p>'),),style='text-align: center'),
            
            Div(
                
          
           
            Field('secret_code',wrapper_class='form-group col-md-12'),
             css_class='form-row'
             ),
           
           
           

            FormActions(
            Div(Div(Submit('save', 'DELETE',css_class="btn-danger"),style='display: inline-block;margin-top:50px;padding:10px;margin-left:10px;'),style='text-align: center'),
              
            )
           ,style="margin: 12px;"),
           
        
        )

    def clean_secret_code(self):
        code = self.cleaned_data.get('secret_code')
        current_question = get_object_or_404(Form, pk=self.instance.pk)
        secret_code = current_question.secret_code_value
        if code!=secret_code:
            raise forms.ValidationError("Invalid Secret Code")
        return code
   