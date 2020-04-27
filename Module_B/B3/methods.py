class Product:
	def __init__(self, name, category, quantity_in_stock):
		self.name = name
		self.category = category
		self.quantity_in_stock = quantity_in_stock

	def is_available(self):
		return True if self.quantity_in_stock > 0 else False

eggs = Product("eggs", "food", 5)
print(eggs.is_available())

class Event:
	def __init__(self, timestamp, event_type, session_id):
		self.timestamp = timestamp
		self.event_type = event_type
		self.session_id = session_id

events = [
    {
     "timestamp": 1554583508000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1555296337000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1549461608000,
     "type": "itemBuyEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]
for event in events:
	event_obj = Event(timestamp = event.get("timestamp"),
	event_type = event.get("type"),
	session_id = event.get("session_id"))
	print(event_obj.timestamp)