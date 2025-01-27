from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s_updated_by', null=True, blank=True)

    class Meta:
        abstract = True
    
class Transaction(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True, related_name='user_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.user}-{self.month}-{self.amount}"