import logging
import sys
from typing import Tuple

import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression

from src.config import config

logger = logging.getLogger(__file__)

try:
    from src.compiled.regressor_pb2 import LinearRegressorState
except ModuleNotFoundError:
    logger.error("Protobuf class has not been generated. Run 'make compile'.")
    sys.exit(1)


def main():
    logger.info("Getting model...")
    model = _get_model()

    logger.info("Loading training dataset...")
    X, y = _load_training_dataset()

    logger.info("Training model...")
    model.fit(X, y)

    logger.info("Saving model state...")
    _save_state(model)


def _get_model() -> LinearRegression:
    return LinearRegression()


def _load_training_dataset() -> Tuple[np.ndarray, np.ndarray]:
    diabetes = load_diabetes()
    return diabetes.data, diabetes.target


def _save_state(model: LinearRegression):
    state = LinearRegressorState()
    state.coef.extend(model.coef_)
    state.intercept = model.intercept_

    with open(config.compiled_regressor_path, "wb") as f:
        f.write(state.SerializeToString())


if __name__ == "__main__":
    main()
