Minimal inference scripts fora.... 
# Experimentally Defined Convolutional Neural Network Architecture Variants for Non-temporal Real-time Fire Detection

Tested using Python 3.4.6, [TensorFlow 1.13.0](https://www.tensorflow.org/install/), [tflearn 0.3](http://tflearn.org/) and [OpenCV 3.3.1 / 4.0.x](http://www.opencv.org)



## Abstract:

_"In  this  work  we  investigate  the  automatic  detection  of  fire pixel  regions  in  video  (or  still)  imagery  within  real-time
bounds without reliance on temporal scene information.  As an extension to prior work in the field, we consider the performance  of  experimentally  defined,  reduced  complexity  deep convolutional neural network (CNN) architectures for this task. Contrary to contemporary trends in the field, our work illustrates
maximal accuracy of 0.93 for whole image binary fire detection (1),  with  0.89  accuracy  within  our  superpixel  localization
framework  can  be  achieved (2),  via  a  network  architecture  of significantly reduced complexity. These reduced architectures
additionally  offer  a  3-4  fold  increase  in  computational  performance offering up to 17 fps processing on contemporary
hardware  independent  of  temporal  information (1).    We  show the  relative  performance  achieved  against  prior  work  using
benchmark datasets to illustrate maximally robust real-time fire region detection."_

(1) using InceptionV1-OnFire CNN model (2) using SP-InceptionV1-OnFire CNN model

[Dunnings and Breckon, In Proc. International Conference on Image Processing IEEE, 2018](https://breckon.org/toby/publications/papers/dunnings18fire.pdf)

## Usage
This code requires the models `firenet.tflite` and `FireNet`.
1. run `download-models.sh` to download FireNet
2. run `converter/firenet-conversion.py` to obtain firenet.tflite


---

## Reference:

If making use of this work in any way (including our [pretrained models](http://dx.doi.org/10.15128/r19880vq98m) or [dataset](http://dx.doi.org/10.15128/r2d217qp536)), _you must_ reference the following article in any report, publication, presentation, software release
or any other materials:

[Experimentally defined Convolutional Neural Network Architecture Variants for Non-temporal Real-time Fire Detection](https://breckon.org/toby/publications/papers/dunnings18fire.pdf)
(Dunnings and Breckon), In Proc. International Conference on Image Processing IEEE, 2018.
```
@InProceedings{dunnings18fire,
  author =     {Dunnings, A. and Breckon, T.P.},
  title =      {Experimentally defined Convolutional Nerual Network Architecture Variants for Non-temporal Real-time Fire Detection},
  booktitle =  {Proc. International Conference on Image Processing},
  pages =      {1558-1562},
  year =       {2018},
  month =      {September},
  publisher =  {IEEE},
  doi = 	 {10.1109/ICIP.2018.8451657},
  keywords =   {simplified CNN, deep learning, fire detection, real-time, non-temporal, non-stationary visual fire detection},
}
```

In addition the terms of the [LICENSE](LICENSE) must be adhered to.

### Acknowledgements:

Atharva (Art) Deshmukh (Durham University, _github and data set collation for publication_).

---
