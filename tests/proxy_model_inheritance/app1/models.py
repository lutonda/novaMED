# TODO: why can't I make this ..app2
from app2.models import NiceModel


class ProxyModel(NiceModel):
    class Meta:
        proxy = True
