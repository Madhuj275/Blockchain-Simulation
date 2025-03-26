from django.db import models
import hashlib
import json

class Block(models.Model):
    index = models.AutoField(primary_key=True)
    timestamp = models.FloatField()
    transactions = models.JSONField()
    previous_hash = models.CharField(max_length=64)
    hash = models.CharField(max_length=64)
    nonce = models.IntegerField(default=0)

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def save(self, *args, **kwargs):
        if not self.index:  # Genesis block
            self.hash = self.calculate_hash()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['index']