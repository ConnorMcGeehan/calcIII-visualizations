# Calc III Visualizations — Loss Function Explorer

This repository contains an interactive visualization tool for exploring loss functions in multivariable calculus. The project visualizes a Mean Squared Error (MSE) loss function with an optional quartic penalty term, and displays:

- The loss surface
- The gradient vector
- Level curves

Users can adjust the model weights and penalty parameter to see how the loss function changes and how calculus concepts such as gradients and critical points relate to optimization.

This project was created as the final project for MATH 211 (Calculus III) at Ithaca College.



## Project Features

- 3D visualization of the loss surface
- Level curve plots for geometric interpretation
- Gradient visualization to illustrate optimization behavior
- Interactive sliders for adjusting:
  - Model weights (w1 and w2)
  - Regularization parameter (alpha)



## Dependencies

To run this project locally, you will need:

- Python 3.7 or higher
- The following Python libraries:
  - numpy
  - pandas
  - matplotlib


## Setup Instructions

Follow the steps below after cloning the repository.

### 1. Clone the Repository

```bash
git clone https://github.com/ConnorMcGeehan/calcIII-visualizations.git
cd calcIII-visualizations
```
### 2. Create and activate a virtual environment

macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
Windows:
```bash
venv\Scripts\activate
```
### 3. Install Required Dependencies
```bash
pip install numpy pandas matplotlib
```


## Running the project

```bash
python3 ./src/main.py
```


## Mathematical Overview

This project visualizes a loss function defined over two variables, representing the weights of a simple linear model. Given two input features $X_1$ and $X_2$, the model predicts an output as:

$$\hat{y} = w_1 X_1 + w_2 X_2$$

Model performance is measured using a Mean Squared Error (MSE) loss function with an optional quartic penalty term. The full loss function is:

$$L(w_1, w_2) = \frac{1}{n} \sum_{i=1}^{n} ((w_1 X_{1i} + w_2 X_{2i}) - y_i)^2 + \alpha (w_1^4 + w_2^4)$$

where $w_1$ and $w_2$ are the model weights, $y_i$ are observed outputs, $n$ is the number of observations, and $\alpha$ controls the strength of the penalty.

The gradient of the loss function is computed using partial derivatives:

$$\frac{\partial L}{\partial w_1} = \frac{2}{n} \sum_{i=1}^{n} ((w_1 X_{1i} + w_2 X_{2i}) - y_i) X_{1i} + 4 \alpha w_1^3$$

$$\frac{\partial L}{\partial w_2} = \frac{2}{n} \sum_{i=1}^{n} ((w_1 X_{1i} + w_2 X_{2i}) - y_i) X_{2i} + 4 \alpha w_2^3$$

Critical points occur where both partial derivatives are equal to zero. Since the MSE term and the quartic penalty are both convex, the resulting loss surface has a single global minimum. Restricting the model to two weights makes it possible to visualize the loss surface, level curves, and gradient behavior directly, providing geometric intuition for optimization and gradient descent.

## Report
A detailed project report is in the `reports` directory for more information. The report explains the math behind the model, the data being used, how and why it was created, and includes screenshots of the project in use.
