from tortoise import fields
from tortoise.models import Model
import uuid

class WatchItem(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    title = fields.CharField(max_length=255)
    instance_id = fields.UUIDField(null=True)
    type = fields.CharField(max_length=50)
    is_recommended = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    user_id = fields.UUIDField(null=True)

    class Meta:
        table = "watch_items"