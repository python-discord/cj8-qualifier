import random
from typing import Any, List
import unittest
from dataclasses import dataclass

from qualifier import make_table
from solution import make_table as solution


@dataclass
class TableParams:
    rows: List[List[Any]]
    labels: List[Any] = None
    centered: bool = False


class MakeTableTests(unittest.TestCase):
    """Basic Requirements."""

    def test_001_parameters(self) -> None:
        make_table(
            rows=[
                ["Apple", 5],
                ["Banana", 3],
                ["Cherry", 7],
            ],
        ),
        make_table(
            rows=[
                ["Apple", 5],
                ["Banana", 3],
                ["Cherry", 7],
            ],
            labels=["Fruit", "Tastiness"],
        ),
        make_table(
            rows=[
                ["Apple", 5],
                ["Banana", 3],
                ["Cherry", 7],
            ],
            labels=["Fruit", "Tastiness"],
            centered=True
        )

    def test_002_return_type(self) -> None:
        table = make_table(
            rows=[
                ["Apple", 5],
                ["Banana", 3],
                ["Cherry", 7],
            ],
        )
        self.assertIsInstance(table, str)

    def test_003_creates_rows(self) -> None:
        cases = (
            TableParams(rows=[
                ["Apple", 5],
            ]),
            TableParams(rows=[
                ["Apple", 5],
                ["Banana", 3],
                ["Cherry", 7],
            ]),
            TableParams(rows=[
                ["Apple", 5],
                ["Banana", 3],
                ["Cherry", 7],
                ["Kiwi", 4],
                ["Strawberry", 6]
            ])
        )

        for case in cases:
            self.assertEqual(make_table(**vars(case)), solution(**vars(case)))

    def test_004_creates_cols(self) -> None:
        cases = (
            TableParams(rows=[
                ["Apple", 5, 70],
            ]),
            TableParams(rows=[
                ["Apple", 5, 70, "Red"],
                ["Banana", 3, 5, "Yellow"],
                ["Cherry", 7, 31, "Red"],
            ]),
            TableParams(rows=[
                ["Apple", 5, 70, "Red", 76],
                ["Banana", 3, 5, "Yellow", 8],
                ["Cherry", 7, 31, "Red", 92],
                ["Kiwi", 4, 102, "Green", 1],
                ["Strawberry", 6, 134, "Red", 28]
            ])
        )

        for case in cases:
            self.assertEqual(make_table(**vars(case)), solution(**vars(case)))

    def test_005_creates_label(self) -> None:
        cases = (
            TableParams(
                rows=[
                    ["Apple", 5, 70]
                ],
                labels=["Fruit", "Tastiness", "Sweetness"]
            ),
            TableParams(
                rows=[
                    ["Apple", 5, 70, "Red"],
                    ["Banana", 3, 5, "Yellow"],
                    ["Cherry", 7, 31, "Red"],
                ],
                labels=["Fruit", "Tastiness", "Sweetness", "Colour"]
            ),
            TableParams(
                rows=[
                    ["Apple", 5, 70, "Red", 76],
                    ["Banana", 3, 5, "Yellow", 8],
                    ["Cherry", 7, 31, "Red", 92],
                    ["Kiwi", 4, 102, "Green", 1],
                    ["Strawberry", 6, 134, "Red", 28]
                ],
                labels=["Fruit", "Tastiness", "Sweetness", "Colour", "Smell"]
            )
        )

        for case in cases:
            self.assertEqual(make_table(**vars(case)), solution(**vars(case)))

    def test_006_align_center(self) -> None:
        cases = (
            TableParams(
                rows=[
                    ["Apple", 5, 70]
                ],
                labels=["Fruit", "Tastiness", "Sweetness"],
                centered=True
            ),
            TableParams(
                rows=[
                    ["Apple", 5, 70, "Red"],
                    ["Banana", 3, 5, "Yellow"],
                    ["Cherry", 7, 31, "Red"],
                ],
                labels=["Fruit", "Tastiness", "Sweetness", "Colour"],
                centered=True
            ),
            TableParams(
                rows=[
                    ["Apple", 5, 70, "Red", 76],
                    ["Banana", 3, 5, "Yellow", 8],
                    ["Cherry", 7, 31, "Red", 92],
                    ["Kiwi", 4, 102, "Green", 1],
                    ["Strawberry", 6, 134, "Red", 28]
                ],
                labels=["Fruit", "Tastiness", "Sweetness", "Colour", "Smell"],
                centered=True
            )
        )

        for case in cases:
            self.assertEqual(make_table(**vars(case)), solution(**vars(case)))

    def test_007_column_width_scaling(self) -> None:
        cases = (
            TableParams(
                rows=[
                    ["Pneumonoultramicroscopicsilicovolcanoconiosis"],
                    ["Hippopotomonstrosesquippedaliophobia"],
                    ["Supercalifragilisticexpialidocious"],
                    ["Pseudopseudohypoparathyroidism"],
                    ["Floccinaucinihilipilification"],
                    ["Antidisestablishmentarianism"],
                    ["."]
                ],
                labels=["My Favourite Long Words"],
                centered=True
            ),
            TableParams(
                rows=[
                    ["Pneumonoultramicroscopicsilicovolcanoconiosis"],
                    ["Hippopotomonstrosesquippedaliophobia"],
                    ["Supercalifragilisticexpialidocious"],
                    ["Pseudopseudohypoparathyroidism"],
                    ["Floccinaucinihilipilification"],
                    ["Antidisestablishmentarianism"],
                    ["."]
                ],
                labels=["My Favourite Long Words"],
                centered=False
            ),
            TableParams(
                rows=[
                    ["A"],
                    ["B"],
                    ["C"],
                    ["D"],
                    ["E"],
                    ["F"],
                    ["Pneumonoultramicroscopicsilicovolcanoconiosis"]
                ],
                labels=["Alphabet"],
                centered=True
            ),
            TableParams(
                rows=[
                    ["A"],
                    ["B"],
                    ["C"],
                    ["D"],
                    ["E"],
                    ["F"],
                    ["Pneumonoultramicroscopicsilicovolcanoconiosis"]
                ],
                labels=["Alphabet"],
                centered=False
            ),
        )

        for case in cases:
            self.assertEqual(make_table(**vars(case)), solution(**vars(case)))

    def test_008_other_item_types(self) -> None:
        cases = (
            TableParams(
                rows=[
                    [None, 1, 2.5, None, 32j, '123'],
                ],
                labels=[3, None, 12, "A", 12.6, 12j],
                centered=True
            ),
        )

        for case in cases:
            self.assertEqual(make_table(**vars(case)), solution(**vars(case)))

    def test_009_custom_objects(self) -> None:
        class Fruit:
            def __init__(self, fruit: str):
                self.fruit = fruit

            def __str__(self) -> str:
                return self.fruit

        apple = Fruit("Apple")
        banana = Fruit("Banana")
        cherry = Fruit("Cherry")
        kiwi = Fruit("Kiwi")
        strawberry = Fruit("Strawberry")

        cases = (
            TableParams(
                rows=[
                    [apple, 5, 70]
                ],
                labels=["Fruit", "Tastiness", "Sweetness"],
                centered=True
            ),
            TableParams(
                rows=[
                    [apple, 5, 70, "Red"],
                    [banana, 3, 5, "Yellow"],
                    [cherry, 7, 31, "Red"],
                ],
                labels=["Fruit", "Tastiness", "Sweetness", "Colour"],
                centered=True
            ),
            TableParams(
                rows=[
                    [apple, 5, 70, "Red", 76],
                    [banana, 3, 5, "Yellow", 8],
                    [cherry, 7, 31, "Red", 92],
                    [kiwi, 4, 102, "Green", 1],
                    [strawberry, 6, 134, "Red", 28]
                ],
                labels=["Fruit", "Tastiness", "Sweetness", "Colour", "Smell"],
                centered=True
            )
        )

        for case in cases:
            self.assertEqual(make_table(**vars(case)), solution(**vars(case)))

    def test_010_lots_of_rows(self) -> None:
        rows = []
        for _ in range(25):
            temp = ["Just", "Another", "Row"]
            random.shuffle(temp)
            rows.append(temp)

        self.assertEqual(make_table(rows), solution(rows))
        self.assertEqual(make_table(rows, centered=True), solution(rows, centered=True))

    def test_011_lots_of_columns(self) -> None:
        rows = []
        for _ in range(25):
            temp = ["Just", "Another", "Column"] * 4
            random.shuffle(temp)
            rows.append(temp)

        self.assertEqual(make_table(rows), solution(rows))
        self.assertEqual(make_table(rows, centered=True), solution(rows, centered=True))
