from enums.item_types import ItemTypes
from consts.prices.chemistry_futbin_prices import FUTBIN_CHEMISTRY_STYLE_PRICES


class ConsumableFutbinPriceFactory:
    def __init__(self, item):
        self.item = item

    def get_consumable_futbin_price(self):
        futbin_prices = {
            ItemTypes.CHEMISTRY_STYLE: FUTBIN_CHEMISTRY_STYLE_PRICES.get(self.item['name']),
            #fill the rest array
        }
        return futbin_prices[ItemTypes(self.item['type'])]
