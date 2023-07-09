import logging
import sys
from typing import Tuple


import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

from src.config import config

logger = logging.getLogger(__file__)

try:
    from src.compiled.regressor_pb2 import LinearRegressorState
except ModuleNotFoundError:
    logger.error("Protobuf class has not been generated. Run 'make compile'.")
    sys.exit(1)


def main():
    logger.info("Loading model from state...")
    model = _load_model()

    logger.info("Loading testing dataset...")
    X, y = _load_testing_dataset()

    logger.info("Predicting...")
    predicted = model.predict(X)

    m2_error = mean_squared_error(y, predicted)
    logger.info(f"Mean squared error is: {m2_error}")



def _load_model() -> LinearRegression:
    model = LinearRegression()
    state = _load_model_state()

    model.coef_ = np.array(state.coef)
    model.intercept_ = state.intercept

    return model


def _load_testing_dataset() -> Tuple[np.ndarray, np.ndarray]:
    # Note that this is the same as training dataset.
    # It's **VERY** invalid from a validation standpoint, but it's not the goal
    # of this demo project
    diabetes = load_diabetes()
    return diabetes.data, diabetes.target


def _load_model_state() -> LinearRegressorState:
    state = LinearRegressorState()
    with open(config.compiled_regressor_path, "rb") as f:
        state.ParseFromString(f.read())
    return state


if __name__ == "__main__":
    main()
