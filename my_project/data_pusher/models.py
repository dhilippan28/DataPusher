from django.db import models
import secrets
unique_token = secrets.token_hex(16)

# Create your models here.

class AccountDetails(models.Model):
    account_id = models.IntegerField(unique=True)
    account_name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=100, unique=True)
    app_secret_code = models.CharField(max_length=255, default= unique_token, editable=False)

    def __str__(self):
        return str(self.account_id) + "-"  + self.account_name

    class Meta:
        db_table = 'account_details'

class DestinationDetails(models.Model):
    account_id = models.ForeignKey(AccountDetails, on_delete=models.CASCADE)
    url = models.CharField(max_length=50)
    http_method = models.CharField(max_length=50)
    headers = models.JSONField(max_length=255)
   
    class Meta:
        db_table = 'destination_details'
