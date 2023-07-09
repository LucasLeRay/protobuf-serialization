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
    person = _create_person()
    _write_person(person)


def _create_person():
    return Person(
        name="Lucas",
        age=25,  # time goes by so quickly...
    )


def _write_person(person: Person):
    with open(config.message_path, "wb") as f:
        f.write(person.SerializeToString())


if __name__ == "__main__":
    main()
