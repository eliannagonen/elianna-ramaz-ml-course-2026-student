# HW01 Writeup — Matrices as Transformations

Finish Part 3, then run `uv run --frozen --python 3.11 python analysis.py` to generate `transforms.png`
and the printed values. Answer the three questions below using **your own**
figure and output. Replace each `[your answer here]` with your response.

---

## Question 1 (3 pts)

**What does each transformation change, and what does it preserve?**

Look at the rotation, scaling, and shear panels of your `transforms.png`.
For each of the three transformations, describe in a sentence or two:

- What changed about the arrow (size? angles? direction it points? proportions?).
- What stayed the same.

The first one (rotation) keeps the size and shape the same, but rotates the arrow 60 degrees counterclockwise, so it points up and slightly right. The second one (scaling) keeps the arrow pointing right, but scales its length by 2 and its height by 0.5, so the proportions and the angles of the arrowhead change (it gets sharper). The area stays the same though, because 2 × 0.5 = 1. The third one (shear) slides each point sideways in proportion to its height (x → x + 0.8y), so the arrow leans over. Its height and the points on the x-axis stay put, but the angles change and the slanted edges get a different length. 

---

## Question 2 (3 pts)

**Why are the R @ S and S @ R panels different?**

Both panels apply the *same* two matrices — a $60^\circ$ rotation and a
$(2, 0.5)$ scaling — to the *same* arrow, just in opposite order. Using your
figure and the printed matrices and arrow-tip positions:

- Describe how the two results differ.
- Explain *why* the order changes the outcome. Connect your explanation to the
  principle that $AB \neq BA$ in general. (Hint: in each
  composition, which transformation does the arrow experience first?)

The two panels are different because the order is different. In R @ S the scaling happens first, so the arrow gets stretched along x, and then the rotation turns that long arrow 60 degrees. The tip [3.0, 0.5] lands at [2.78, 5.32], so the arrow points mostly up. In S @ R the rotation happens first, so the arrow already points up and to the right, and then the scaling stretches x and shrinks y. The tip lands at [2.13, 1.42], and the arrow looks flat and squished because the scaling axes no longer line up with the arrow.

This is what AB ≠ BA means. In (R @ S)v, S is applied to v first and then R. In (S @ R)v it's R first and then S. Scaling only stretches along the x and y axes, so what it does to the arrow depends on which way the arrow is pointing when it happens. The printed matrices are different too: R @ S = [[1, -0.433], [1.732, 0.25]] and S @ R = [[1, -1.732], [0.433, 0.25]]. They would only match if the scaling were the same on both axes, because then direction wouldn't matter.

---

## Question 3 (4 pts)

**What does the matrix part of a dense neural-network layer do?**

A dense layer uses a weight matrix to transform its input vectors. Here,
consider only that matrix operation, before adding a bias or applying a
nonlinearity. Your Part 3 figure shows several $2 \times 2$ examples.

Using your own figure and printed output, explain:

- Choose one panel and describe what its matrix did geometrically. If $X$
  stores $N$ two-dimensional points as rows and the weight matrix $W$ has
  shape $(2, 2)$, what shape should the transformed points have? Explain how
  storing points in rows fits the lecture's column-vector expression $Wp$.
- Why can changing the order of two weight matrices change the output?
  Support your answer with your two arrow-tip positions from Question 2,
  identifying which transformation acts first in each composition.

I'll use the R @ S panel (scale, then rotate). Its matrix is [[1, -0.433], [1.732, 0.25]]. Each column of the matrix shows where one axis direction ends up. The first column, [1, 1.732], is where the x direction goes, so it now points up and to the right. The second column, [-0.433, 0.25], is where the y direction goes. So the whole grid gets tilted and stretched, and the arrow goes with it. For the tip [3.0, 0.5], the new x is 1 × 3 + (-0.433) × 0.5 ≈ 2.78 and the new y is 1.732 × 3 + 0.25 × 0.5 ≈ 5.32, which matches the printed [2.78, 5.32].

If X holds N points as rows, its shape is (N, 2). W is (2, 2), and a 2×2 matrix takes a 2D point to another 2D point, so the output is also (N, 2). A matrix times a single point is usually written Wp, with p as a column. But my points are rows, so I take the transpose: (Wp)^T = p^T W^T. Doing that for all N points at once gives Y = X @ W.T, so row i of Y is the transformed version of row i of X. (If code does X @ W, it's really applying W^T.)

The order matters because two weight matrices in a row work like two layers back to back. In W2 W1 p, the point goes through W1 first and then W2. In my output, R @ S scales first and then rotates, and the tip [3.0, 0.5] lands at [2.78, 5.32]. S @ R rotates first and then scales, and the same tip lands at [2.13, 1.42]. Scaling only stretches along the x and y axes, so if the arrow is still pointing along x it just gets longer, but after a rotation the same scaling stretches it a different way. So the matrices can't be swapped without changing the output, and the same goes for the order of weights in a network.