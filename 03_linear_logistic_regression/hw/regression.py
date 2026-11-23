"""HW03 - Linear and Logistic Regression.

Implement the spec in spec.pdf. The public API of this file is:

    sigmoid(z)
    LinearModel       (shared base class)
    LinearRegression  (subclass of LinearModel)
    LogisticRegression(subclass of LinearModel)

Restrictions: no torch.autograd, no .backward(), no sklearn.linear_model.

Run tests:   uv run pytest
Check score: uv run python score.py
"""

from __future__ import annotations

import torch


def sigmoid(z: torch.Tensor) -> torch.Tensor:
    """See spec.pdf section 2 (standalone sigmoid)."""
    return 1 / (1 + torch.exp(-z))

class LinearModel:
    """See spec.pdf section 3 (shared LinearModel base class)."""
    def __init__(self, n_features: int, lr: float = 0.1) -> None:
        self.w = torch.zeros(n_features)
        self.b = torch.tensor(0.0)
        self.lr = lr

    def gradient(self, X: torch.Tensor, y_true: torch.Tensor, y_pred: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        r = y_pred - y_true
        n = X.shape[0]
        dw = (1/n) * X.T @ r
        db = (1/n) * torch.sum(r)
        return dw, db

    def fit(self, X: torch.Tensor, y: torch.Tensor, epochs: int = 200) -> list[float]:
        history = []
        for epoch in range(epochs):
            y_pred = self.forward(X)
            y_true = y

            loss = self.loss(y_pred, y_true)
            history.append(loss.item())

            dw, db = self.gradient(X, y_true, y_pred)

            self.w -= self.lr * dw
            self.b -= self.lr * db

        return history

    def predict(self, X: torch.Tensor) -> torch.Tensor:
        return self.forward(X)

class LinearRegression(LinearModel):
    """See spec.pdf section 4 (LinearRegression: forward + MSE loss)."""
    def forward(self, X: torch.Tensor) -> torch.Tensor:
        y = X @ self.w + self.b
        return y

    def loss(self, y_pred: torch.Tensor, y_true: torch.Tensor) -> torch.Tensor:
        mse = (1/2) * torch.mean((y_pred - y_true)**2)
        return mse

class LogisticRegression(LinearModel):
    """See spec.pdf section 5 (LogisticRegression: forward, BCE, predict)."""
    def forward(self, X: torch.Tensor) -> torch.Tensor:
        y = X @ self.w + self.b
        return sigmoid(y)

    def loss(self, y_pred: torch.Tensor, y_true: torch.Tensor) -> torch.Tensor:
        epsilon = 10**-7
        clamped_y_pred = torch.clamp(y_pred, min=epsilon, max=1-epsilon)
        bce = -torch.mean(y_true * torch.log(clamped_y_pred) + (1 - y_true) * torch.log(1 - clamped_y_pred))
        return bce

    def predict_proba(self, X: torch.Tensor) -> torch.Tensor:
        return self.forward(X)

    def predict(self, X: torch.Tensor) -> torch.Tensor:
        probabilities = self.predict_proba(X)
        return (probabilities > 0.5).to(torch.float32)