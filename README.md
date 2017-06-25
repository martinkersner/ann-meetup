# Artificial Neural Networks

Martin Kersner, <m.kersner@gmail.com>

Practice of implementing Multilayer Perceptron trained with Stochastic Gradient Descent for [Seoul AI Meetup](https://www.meetup.com/Seoul-Artificial-Intelligence-Meetup/) on June 25, 2017.
Implementation is within [Jupyter notebook](https://github.com/martinkersner/ann-meetup/blob/master/ann.ipynb).

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
