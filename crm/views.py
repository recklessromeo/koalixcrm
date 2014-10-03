# -*- coding: utf-8 -*-
from os import path

from django.core.servers.basehttp import FileWrapper
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from crm.models import *


def export_pdf(calling_model_admin, request, where_to_create_from, what_to_create, redirect_to):
    """This method exports PDFs provided by different Models in the crm application

        Args:
          calling_model_admin (ModelAdmin):  The calling ModelAdmin must be provided for error message response.
          request: The request User is to know where to save the error message
          where_to_create_from (Model):  The model from which a PDF should be exported
          what_to_create (str): What document Type that has to be
          redirect_to (str): String that describes to where the method sould redirect in case of an error

        Returns:
              HTTpResponse with a PDF when successful
              HTTpResponseRedirect when not successful

        Raises:
          raises Http404 exception if anything goes wrong"""
    try:
        pdf = where_to_create_from.create_pdf(what_to_create)
        response = HttpResponse(FileWrapper(file(pdf)), mimetype='application/pdf')
        response['Content-Length'] = path.getsize(pdf)
    except Exception, e:  # (TemplateSetMissing, UserExtensionMissing, CalledProcessError), e:
        # if type(e) == UserExtensionMissing:
        # response = HttpResponseRedirect(redirect_to)
        #     calling_model_admin.message_user(request, trans("User Extension Missing"))
        # elif type(e) == TemplateSetMissing:
        #     response = HttpResponseRedirect(redirect_to)
        #     calling_model_admin.message_user(request, trans("Templateset Missing"))
        if type(e) == CalledProcessError:
            response = HttpResponseRedirect(redirect_to)
            calling_model_admin.message_user(request, e.output)
        else:
            raise Http404
    return response


def selectaddress(invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    address = invoice.contract
  

  
   