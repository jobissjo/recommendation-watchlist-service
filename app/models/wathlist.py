from tortoise import fields
from tortoise.models import Model

class WatchItem(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    instance_id = fields.UUIDField(null=True)
    type = fields.CharField(max_length=50)
    is_recommended = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "watch_items"