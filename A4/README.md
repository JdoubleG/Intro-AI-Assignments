James Garijo-Garde
4/18/2019

Comp131 Homework 4

This is a program that classifies Iris flowers based on several features of the
flowers.

Neural Network Layout:
  * 3 Neurons
  * Neuron 0 Input: Sepal Length, Sepal Width
  * Neuron 1 Input: Petal Length, Petal Width
  * Neuron 2 Input: Neuron 0 Output, Neuron 1 Output
  * Eta (n) = .1
  * Initial Weights = randomly assigned and ranging from -1/8 to +1/8
  * Sigmoid Activation Function
  * Training/Validation cycle stops if training error or validation error 
    increases or if 200 cycles have passed

How to run: type "python3 ANN.py" into your command line. Be sure Neuron.py is
            in the same directory. The program will automatically train and
            validate until the ANN is ready for testing (testing is also
            automatic). The user will then have the opportunity to input custom
            input for classification.