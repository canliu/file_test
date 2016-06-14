import xml.etree.cElementTree as ET
#x=ET.tostring('xml',encoding='utf-8')
root=ET.Element('AmazonEnvelope')
root.set('xmlns:xsi1','http://www.w3.org/2001/XMLSchema-instance')
root.set('xsi:noNamespaceSchemaLocatio','amznenvelope.xsd')
header=ET.SubElement(root,'Header')
ET.SubElement(header,'DocumentVersion').text='1.01'
ET.SubElement(header,'MerchantIdentifier').text='M_seller'
ET.SubElement(root,'MessageType').text='Inventory'
id=0
for sku in range(100000):
    id+=1
    message=ET.SubElement(root,'Message')
    ET.SubElement(message,'MessageID').text=str(id)
    ET.SubElement(message,'OperationType').text='Update'
    inventory=ET.SubElement(message,'Inventory')
    ET.SubElement(inventory,'SKU').text='sku'+str(sku)
    ET.SubElement(inventory,'Quantity').text='3'
    ET.SubElement(inventory,'FulfillmentLatency').text='6'

#print(ET.tostring(root))
with open('file.xml','wb') as f:
    f.write(b'<xml version="1.0" encoding="utf-8" ?>')
    f.write(ET.tostring(root).replace(b'><',b'>\n<'))

