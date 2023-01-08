from sellpass import SellPass

api_key = " " #https://dashboard.sellpass.io/settings/security
product_id = 51890 #https://dashboard.sellpass.io/products/all-products
shop_id = 6951 # Inspect F12 your shop your id is in _NEXT_DATA_  -> MainDetails

add_serials = [
    "id3:pass3",
    "id4:pass4"
    ]

client = SellPass(api_key, shop_id)
try:
    data = client.get_productv2(product_id)
except Exception as e:
    print("An error occurred while trying to retrieve product data:", e)
    exit()

try:
    serials = data["product"]["variants"][0]["asSerials"]["serials"]
    print("Old Serials are: ",serials)
    serials.extend(add_serials)
    data["product"]["variants"][0]["asSerials"]["serials"] = serials
    print("New Serials are: ",serials)
except Exception as e:
    print("An error occurred while trying to update serial keys:", e)
    exit()

title = data["product"]["title"]
description = data["product"]["description"]
variants = data["product"]["variants"]
path = data["path"]
seo = data["seo"]

try:
    client.edit_productv2(
        product_id = product_id,
        title = title,
        description = description,
        variants = variants,
        path = path,
        seo = seo,
        )
except Exception as e:
    print("An error occurred while trying to edit the product:", e)
    exit()
    
print("Product successfully edited!")