import logging
import sys

from src.config import config

logger = logging.getLogger(__file__)

try:
    from src.compiled.person_pb2 import Person
except ModuleNotFoundError:
    logger.error("Protobuf class has not been generate. Run 'make compile'.")
    sys.exit(1)


def main():
    person = _read_person()
    logger.info(f"Name is '{person.name}' and age is '{person.age}'")


def _read_person() -> Person:
    person = Person()
    with open(config.message_path, "rb") as f:
        person.ParseFromString(f.read())
    return person


if __name__ == "__main__":
    main()
