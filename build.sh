#!/usr/bin/sh

python3 -m pip install -r requirements.txt

sudo cp ~/.local/bin/normalizer /usr/bin/
sudo cp ~/.local/bin/pyi-bindepend /usr/bin/
sudo cp ~/.local/bin/pyi-makespec /usr/bin/
sudo cp ~/.local/bin/pyi-set_version /usr/bin/
sudo cp ~/.local/bin/pyi-archive_viewer /usr/bin/
sudo cp ~/.local/bin/pyi-grab_version /usr/bin/
sudo cp ~/.local/bin/pyinstaller /usr/bin/

pyinstaller --icon yandere.ico --onefile yandere-dl.py

sudo chmod a+rwx ./dist/yandere-dl

echo 'Build has completed. Binary is inside of the dist folder.'
