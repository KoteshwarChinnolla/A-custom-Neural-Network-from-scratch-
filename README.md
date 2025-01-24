# A-custom-Neural-Network-from-scratch

This is divided into mainly 3 parts.

> 1. Machine Learning
> 2. Using Keras
> 3. Using a Custom Model


### *creating a Custom Model is the main aim of this Repo*

You can have a look at all the theories [Here](https://github.com/KoteshwarChinnolla/A-custom-Neural-Network-from-scratch-/blob/main/theory_Neural_network.ipynb). where I followed all maths to create a model

It is always fascinating to implement what we have learnt theoretically. It would be way more interesting if we tried to build something that amazed us some time back. 

If you want to have a look at the process I followed while building it, [Visit](https://github.com/KoteshwarChinnolla/A-custom-Neural-Network-from-scratch-/blob/main/deep_leaqrning%20copy.ipynb). This includes implementing maths to automate whole processes.

The model I built is over [here](https://github.com/KoteshwarChinnolla/A-custom-Neural-Network-from-scratch-/tree/main/customNNs)

Training a Neural Network follows
>[!IMPORTANT]
> 1. Model Creation
> 2. Assigning Weights and Biases
> 3. Forward Propagation
> 4. Loss Calculation
> 5. Backwards Propagation
> 6. Making Loss Lower (Gradient Docent)
> 7. Optimization (Application of gradient descent in different ways)

We are now following the same 7 steps in every file to create a custom Model.
### Theoretical initiation 
1. Understanding theory [theory_Neural_network. ipynb](https://github.com/KoteshwarChinnolla/A-custom-Neural-Network-from-scratch-/blob/main/theory_Neural_network.ipynb ): Every step is explained using the Product Demand DataSet. This file mainly includes the Mathematical equations and converting them into code for implementation. For this, we all need numpy. Starting from model creation with random weights to back-propagating for reduction of loss. We follow the same steps as mentioned abo
### Automation 
2. Till now we just created a pre-planned architecture, here we just planned the number of hidden layers the model must contain and the number of Neurans each hidden layer has. In this case, every time we want to use more hidden layers or more neurons in the architecture. We just need to interrupt the code. This doesn't make any sense. Here we must look at the automaton. Automating the process of self-creation and assignment of Hidden layers and neurons will make our tasks a lot easier. This may also help in the easy access of the model. To implement this we need to look at the patterns the code is following every time we create each hidden layer. Running Loops every time we add more hidden layers or neurons. Rather every time we are colling above mentioned 7 steps is something that increases the code length. Making the model something that auto-assigns the weights and follows all 7 steps just by inputting the architecture in the function train makes all our tasks much faster and easier. th file [Automation](https://github.com/KoteshwarChinnolla/A-custom-Neural-Network-from-scratch-/blob/main/deep_leaqrning%20copy.ipynb) is all about it.
