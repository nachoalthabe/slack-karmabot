"""
Recive un json tipo
   {
        "token": "Jhj5dZrVaK7ZwHHjRyZWjbDl",
        "challenge": "3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P",
        "type": "url_verification"
    }
y responde un 200 con el contenido de challenge
+i: https://api.slack.com/events-api#subscriptions
"""

def process(path, data):
    """Aca no se jode..."""
    return data['challenge']