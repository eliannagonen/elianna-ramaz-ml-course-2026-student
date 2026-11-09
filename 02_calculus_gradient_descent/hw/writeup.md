# HW02 Writeup — Derivatives and Autograd

After implementing all six functions, run the comparison script:

```bash
uv run --frozen --python 3.11 python derivatives.py
```

It prints a side-by-side table of your manual gradients and your autograd
gradients. Use that output to answer the three questions below. Replace each
`[your answer here]` with your response.

---

## Question 1 (3 pts)

**Do your manual and autograd gradients agree?**

Paste (or neatly transcribe) the comparison table printed by
`uv run --frozen --python 3.11 python derivatives.py`. Then answer:

- Do the manual and autograd values agree, allowing for floating-point
  rounding, at **every** point in the table?
- If any pair disagreed at some point while you were developing your
  solutions, what was the bug, and how did the table (or the tests) help you
  find it? If they agreed on your first try, say so — and describe one
  specific mistake the table *would* have caught (for example, in which rows
  the numbers would split apart if you forgot part of a derivative rule).

function @ point                                   manual     autograd     |diff|
---------------------------------------------------------------------------------
quadratic   a=1, b=0, x=2                          4.0000       4.0000   0.00e+00
quadratic   a=3, b=2, x=1                          8.0000       8.0000   0.00e+00
quadratic   a=-2, b=5, x=1                         1.0000       1.0000   0.00e+00
quadratic   a=0.5, b=-1, x=4                       3.0000       3.0000   0.00e+00
composite   x=0                                    0.0000       0.0000   0.00e+00
composite   x=1                                   18.0000      18.0000   0.00e+00
composite   x=2                                  240.0000     240.0000   0.00e+00
composite   x=-1                                   6.0000       6.0000   0.00e+00
partial df/dx  (x,y)=(1,2)                         8.0000       8.0000   0.00e+00
partial df/dy  (x,y)=(1,2)                        11.0000      11.0000   0.00e+00
partial df/dx  (x,y)=(2,1)                         7.0000       7.0000   0.00e+00
partial df/dy  (x,y)=(2,1)                        10.0000      10.0000   0.00e+00
partial df/dx  (x,y)=(0,0)                         0.0000       0.0000   0.00e+00
partial df/dy  (x,y)=(0,0)                         0.0000       0.0000   0.00e+00
partial df/dx  (x,y)=(-1,3)                        7.0000       7.0000   0.00e+00
partial df/dy  (x,y)=(-1,3)                        9.0000       9.0000   0.00e+00
---------------------------------------------------------------------------------

The manual and autograd values agreed on my first try. If I had forgotten to apply the chain rule when differentiating the composite function, the values in the composite rows would have disagreed. The comparison table would have helped me identify that my manual derivative was missing the derivative of the inner function.

---

## Question 2 (4 pts)

**The chain rule, by hand and by `.backward()`.**

Take the composite function from this assignment, $f(x) = (x^3 + 2)^2$.

**a)** Write out the chain-rule steps you used in
`manual_gradient_composite`: identify the outer function and the inner
function, give the derivative of each, and show how they combine into
$f'(x)$.

**b)** Now explain what PyTorch is doing when `autograd_gradient_composite`
runs its backward pass. Autograd is bookkeeping of the
chain rule over a computation graph — walk through how *your* steps from
part (a) show up in that process: what operations get recorded as you build
`f` from the input, and how the backward pass combines their derivatives to
produce the gradient stored on your input tensor.

a) u = x^3 + 2 is the inner function and f = u^2 is the outer function. The derivative of u is 3x^2 and the derivative of f is 2u. The chain rule says the derivative becomes f' times u' = 2(x^3 + 2) · 3x^2 = 6x^2(x^3 + 2). 

b) In the forward pass, PyTorch records every operation done to the tensor (x) in a computation graph as it builds the function (f). It starts with the power operation (x^3), then the addition (x^3+2), then the power operation ((x^3+2)^2). In the backward pass, PyTorch starts at the last operation, takes the derivative of the outer operation [2u] and the inner operation [3x^2], and then applies the chain rule. The chan rule multiplies the derivatives of the inner and outer operation to compute the gradient [2(x^3+2) · 3x^2] , which is stored in x.grad. 

---

## Question 3 (3 pts)

**From your gradient to a parameter update.**

**a) One update (1 pt).** Use the row for the composite function at $x=1$
from **your** comparison table. State the gradient value $g$ you obtained,
then compute one update $x_{new}=1-0.01g$. Explain why your step moves left
or right.

**b) A gradient error (1 pt).** Suppose the gradient used in that same step
were $g+2$ instead. Compute the new update and its difference from part (a).
Does this error change the direction, the distance, or both? A different
step is not automatically worse; explain what you can conclude from this
calculation without running further steps.

**c) Choosing a method (1 pt).** Suppose you want the gradient of a scalar
function with $d$ inputs. Compare estimating each partial derivative using
forward differences with computing the gradient using PyTorch autograd:

- How many function evaluations would forward differences require if you
  reuse the value at the original input? How does autograd avoid repeating
  that work separately for each input?
- Which source of error does autograd avoid, and why are its results still
  not perfectly exact?

Refer to the lecture box **“Why not estimate derivatives from nearby values?”**
if needed.

a)  I got g = 18. $x_{new}$ = 1 - (0.01)g = 1 - (0.01)(18) = 1 - 0.18 = 0.82. Since the gradient is positive, the update decreases x, moving left.
  
b)  If the new gradient was g+2 = 18+2 = 20, the $x_{new}$ = 1 - (0.01)g = 1 - (0.01)(20) = 1 - 0.20 = 0.80. The new update is 0.02 smaller than part (a). The error does not change the direction because both gradients are positive, but it increases the distance of the step. 
  
c) 