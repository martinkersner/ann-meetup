# Artificial Neural Networks - Seoul AI Meetup Practice
Martin Kersner, <m.kersner@gmail.com>

## Get repository
```
git clone https://github.com/martinkersner/ann-meetup.git
```

## Virtualenv
``` bash
virtualenv -p /usr/bin/python2.7 venv # Python 2 is required
source venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

## Troubleshooting
If `jupyter notebook` is complaning about protobuf, try to run this command.
```bash
pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/protobuf-3.1.0-cp27-none-linux_x86_64.whl
```
