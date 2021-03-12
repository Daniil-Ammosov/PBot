from aiogram.types import ShippingOption, LabeledPrice

# Label for shipping options
LICENSE = LabeledPrice(label="Персональная лицензия", amount=1500 * 100)
HELPING = LabeledPrice(label="Персональная поддержка", amount=2000 * 100)

# Some shipping option
OPTION =  ShippingOption(id='new_license', title='Лицензия на допуск')
OPTION.add(LICENSE)
OPTION.add(HELPING)
