# Adversarial-Machine-Learning-Attacks-on-Homomorphic-Encryption #
The repository contains experimental results of the thesis. Model extraction and inversion codes are in their respective folders.
The extraction and inversion attack codes are in .ipynb files. To run the files, open them in Google Colab and from runtime select Restart and run all. The first cell of all the files will install the required dependencies. To save the extracted images, modify the path in model inversion .ipynb files.
## PRADA ##
The code for PRADA: Protecting Against DNN Model Stealing Attacks is in the respective folder. The code cannot be run on Colab and hence a setup is required.
### Requirements ###
* Python3
* PyTorch
* torchvision
* numpy
* scipy
* matplotlib
* flask
* requests
<br />
Install the above using conda or pip.
<br />

## Usage ##
<br />
All the code files are present in src folder. The data folder contains datasets that can be used to query the target model.
<br />
Use model.py to create a target model. Use traincnn.ipynb to train and save the target model.
<br />
In main.py, provide the path of the saved target model.
<br />
Execute main.py to create a server. Then in another terminal execute run.py to query the model. run.py can be modeified to use any dataset. The code works with images in MNIST format i.e., (28,28). If an attack is detected, the server will return shuffled probability vector.


## References
<a id="1">[1]</a> 
GitHub - Koukyosyumei. 
AIJack: Security and Privacy Risk Simulator for Machine Learning. 
https://github.com/Koukyosyumei/AIJack

<a id="2">[2]</a> 
Trusted-AI/adversarial-robustness-toolbox: Adversarial Robustness Toolbox (ART) - Python Library for Machine Learning Security - Evasion, Poisoning, Extraction, Inference
https://github.com/Trusted-AI/adversarial-robustness-toolbox
