# HW03 Writeup — Linear and Logistic Regression

Run `uv run python analysis.py` to generate your results, then answer the
questions below. Replace each `[your answer here]` with your actual response.

---

## Question 1 (3 pts): Learning Rate Effects

**Run `analysis.py`. It trains your linear regression model with three learning
rates: `lr=2e-5`, `lr=0.02`, and `lr=1.0`. Look at the `loss_curve.png` plot
and the printed loss values.**

**a)** Describe what the loss curve looks like for each learning rate.
What happens to the loss over the 200 epochs in each case?

The loss curve with the learning rate of 2e-5 is a  straight line with a relatively constant error at ~2.8. The loss curve with the learning rate of 0.02 is a consistently downward sloping curve whose error starts at 2.8 but decreases to a minimum of 0.3 over the 200 epochs. The loss curve with the learning rate of 1 sharply decreases to 0.26 before gradually increasing over the 200 epochs. 

**b)** Which learning rate worked best within these 200 epochs? Describe what
the other runs suggest about steps that are too small or too large. Use
specific numbers from your printed output to support your answer.

The learning rate of 0.02 worked best because it achieved the smallest loss within 200 epochs. The learning rate of 1 was too large because the model took steps that were too large (overshot the minimum), moving from 2.8 sharply down to 0.26 and then back up to 19.8. The learning rate of 2e-5 was too small because the model took steps that were too small and didn't make any meaningful progress toward the minimum. 

---

## Question 2 (3 pts): The Decision Boundary

**Look at your `decision_boundary.png` and the printed learned parameters
`w = [w1, w2]` and `b`.**

**a)** The decision boundary is the line where $\hat{y} = 0.5$, which means
$\sigma(x_1 w_1 + x_2 w_2 + b) = 0.5$.
Since $\sigma(z) = 0.5$ exactly when $z = 0$, the boundary satisfies:

$$x_1 w_1 + x_2 w_2 + b = 0$$

Using your actual trained values of $w_1$, $w_2$, and $b$, rewrite this as a
line equation in the form $x_2 = m x_1 + c$.
What are $m$ and $c$ in terms of $w_1$, $w_2$, and $b$?
If $w_2 = 0$, describe the boundary directly from the equation instead.

$x_2 = -\frac{w_1}{w_2}x_1 - \frac{b}{w_2} = \frac{4.4866}{3.2822}x_1 + \frac{0.7950}{3.2822} = 1.3669x_1 + 0.2422$

$m = -\frac{w_1}{w_2}$
$c = -\frac{b}{w_2}$

If $w_2 = 0$:
$x_1 w_1 + b = 0$  
$x_1 = -\frac{b}{w_1}$

**b)** The plot shows the test points. How many of those points did the model
misclassify? Use the plot and the test accuracy to explain what you can conclude about how well the model generalized to held-out examples.

The model correctly classified all 20 examples (0 errors) with a test accuracy of 100%. The model was given 20 new examples and was able to classify them all correctly, so it seems to have generalized very well to this test set. It also says that if the model just predicted the most common training class (training majority baseline), it would have only been 40% accurate on the test set. 

---

## Question 3 (4 pts): One Gradient, Two Models

**Your base class `LinearModel` has a single `gradient` method, yet it correctly
trains both `LinearRegression` and `LogisticRegression`. That works because both
gradients reduce to the exact same formula:**

$$\frac{\partial L}{\partial \mathbf{w}} = \frac{1}{n} X^\top (\hat{\mathbf{y}} - \mathbf{y})$$

**a)** Linear regression uses `MSE = (1/2n) sum (yhat_i - y_i)^2`. Differentiate
the squared error term $(\hat{y}_i - y_i)^2$ with respect to $w_j$ and show how
the factor of 2 from the power rule cancels the $1/2$ in front, leaving the
formula above. Where would an extra factor of 2 appear if you had **not**
included the $1/2$?

The derivative of $(\hat{y}_i - y_i)^2$ with respect to $\hat{y}_i$ is: 2$(\hat{y}_i - y_i)$
The derivative of $\hat{y}_i$ with respect to $w_j$ is: $x_{ij}$

To get the derivative of $(\hat{y}_i - y_i)^2$ with respect to $w_j$, you have to multiply the two derivatives together (chain rule) which is: 2$x_{ij}(\hat{y}_i - y_i)$

Including the $\frac{1}{2n}$ from the loss (factor of 2 cancels with the $\frac{1}{2}$): $\frac{1}{n}\sum x_{ij}(\hat{y}_i - y_i)$

If you didn't include the $\frac{1}{2}$, there would be a remaining factor of 2 in front of the gradient.

**b)** Logistic regression uses binary cross-entropy with no $1/2$ factor, yet
its gradient is the *same* formula. Work through the BCE gradient yourself and explain in one or two sentences what
cancels in the BCE case so that no factor of 2 (and no leftover $\sigma'(z)$
term) survives.

The BCE loss for one example is: $L_i=-y_i\log(\hat{y}_i)-(1-y_i)\log(1-\hat{y}_i)$, where $\hat{y}_i$ = $\sigma(z_i)$

The derivative of $L_i$ with respect to $\hat{y_i}$ is: $ -\frac{y_i}{\hat{y}_i} + \frac{1-y_i}{1-\hat{y}_i}$
The derivative of $\hat{y_i}$ with respect to $z_i$ is: $\hat{y}_i(1-\hat{y}_i)$
The derivative of $z_i$ with respect to $w_{ij}$ is: $x_{ij}$

To get the derivative of $L_i$ with respect to $w_{ij}$, you have to multiply the three derivatives together (chain rule) which is: $x_{ij}(\hat{y}_i - y_i)$
The average over all $n$ examples would be: $\frac{1}{n}\sum x_{ij}(\hat{y}_i - y_i)$

The BCE and sigmoid derivatives cancel each other out, leaving $(\hat y_i-y_i)$. Unlike MSE, there is no factor of 2.

## Question 4 (3 pts): The Number You Have To Beat

**Before it trains the Iris model, `analysis.py` finds the most common class
in the training labels. The baseline always predicts that class and evaluates
those predictions on the test split.**

**a)** Report the baseline and model accuracies on the **test** split.
What is their difference in percentage points, and which scored higher?

The baseline had a test accuracy of 40%, while the model had an accuracy of 100%, a difference of 60 percentage points. 

**b)** Why is a constant prediction a meaningful comparison? Consider another
dataset where class 0 is the training majority and accounts for 95 of the 100
test labels. If a model reported 94% test accuracy, what would you conclude
from comparing it with the baseline?

The constant prediction is a meaningful comparison because it shows whether your model is learning something useful by comparing its performance to a simple majority-class baseline. Even though a model that reports 94% test accuracy seems impressive, the trained model actually performs worse than simply predicting the majority class every time (95% accuracy). The model has not demonstrated that it is more useful than the baseline for distinguishing classes.
