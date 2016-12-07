rm -rf /tmp/ovpn*
rm -rf /tmp/base64.txt
cd /home/sick/vg_midser/midser
python3 ./mainline.py
cp /tmp/base64.txt /home/sick/vg_midser/static/base64.txt
date
