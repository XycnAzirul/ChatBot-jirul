import os

TOKEN = os.environ.get("TOKEN", None) # Dapatkan di @botfather
OWNER = os.environ.get("OWNER", "azirulfariq") # Isi dengan username kalian tanpa tanda @
GROUP = os.environ.get("GROUP", "temanbercakapofficial") # Isi dengan username group kalian tanpa tanda @ kalau gak punya gak usah isi
CHANNEL = os.environ.get("CHANNEL", "azirul_fariq") # Isi dengan username channel kalian tanpa tanda @ kalau gak punya gak usah isi
DB_URI = os.environ.get("DATABASE_URL", "")
