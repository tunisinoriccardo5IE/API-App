
# install the compatible telegram library (v13.x used by Updater/CallbackContext API)

python -m pip install "python-telegram-bot==13.7"



# ensure it's recorded in requirements.txt

mkdir -p "$(dirname requirements.txt)" || true

touch requirements.txt

grep -qxF "python-telegram-bot==22.5" requirements.txt || echo "python-telegram-bot==22.5" >> requirements.txt
