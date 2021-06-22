from typing import Any, List
import unittest
from dataclasses import dataclass

from qualifier import make_table


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
        self.assertIsInstance(table, str, msg="The return type from your solution does not seem to be a string.")

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

        expected = (
            '┌───────┬───┐\n'
            '│ Apple │ 5 │\n'
            '└───────┴───┘',

            '┌────────┬───┐\n'
            '│ Apple  │ 5 │\n'
            '│ Banana │ 3 │\n'
            '│ Cherry │ 7 │\n'
            '└────────┴───┘',

            '┌────────────┬───┐\n'
            '│ Apple      │ 5 │\n'
            '│ Banana     │ 3 │\n'
            '│ Cherry     │ 7 │\n'
            '│ Kiwi       │ 4 │\n'
            '│ Strawberry │ 6 │\n'
            '└────────────┴───┘'
        )

        for case, expect in zip(cases, expected):
            self.assertEqual(make_table(**vars(case)), expect, msg="Failed when creating multiple rows.")

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

        expected = (
            '┌───────┬───┬────┐\n'
            '│ Apple │ 5 │ 70 │\n'
            '└───────┴───┴────┘',

            '┌────────┬───┬────┬────────┐\n'
            '│ Apple  │ 5 │ 70 │ Red    │\n'
            '│ Banana │ 3 │ 5  │ Yellow │\n'
            '│ Cherry │ 7 │ 31 │ Red    │\n'
            '└────────┴───┴────┴────────┘',

            '┌────────────┬───┬─────┬────────┬────┐\n'
            '│ Apple      │ 5 │ 70  │ Red    │ 76 │\n'
            '│ Banana     │ 3 │ 5   │ Yellow │ 8  │\n'
            '│ Cherry     │ 7 │ 31  │ Red    │ 92 │\n'
            '│ Kiwi       │ 4 │ 102 │ Green  │ 1  │\n'
            '│ Strawberry │ 6 │ 134 │ Red    │ 28 │\n'
            '└────────────┴───┴─────┴────────┴────┘'
        )

        for case, expect in zip(cases, expected):
            self.assertEqual(make_table(**vars(case)), expect, msg="Failed when creating multiple columns.")

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

        expected = (
            '┌───────┬───────────┬───────────┐\n'
            '│ Fruit │ Tastiness │ Sweetness │\n'
            '├───────┼───────────┼───────────┤\n'
            '│ Apple │ 5         │ 70        │\n'
            '└───────┴───────────┴───────────┘',

            '┌────────┬───────────┬───────────┬────────┐\n'
            '│ Fruit  │ Tastiness │ Sweetness │ Colour │\n'
            '├────────┼───────────┼───────────┼────────┤\n'
            '│ Apple  │ 5         │ 70        │ Red    │\n'
            '│ Banana │ 3         │ 5         │ Yellow │\n'
            '│ Cherry │ 7         │ 31        │ Red    │\n'
            '└────────┴───────────┴───────────┴────────┘',

            '┌────────────┬───────────┬───────────┬────────┬───────┐\n'
            '│ Fruit      │ Tastiness │ Sweetness │ Colour │ Smell │\n'
            '├────────────┼───────────┼───────────┼────────┼───────┤\n'
            '│ Apple      │ 5         │ 70        │ Red    │ 76    │\n'
            '│ Banana     │ 3         │ 5         │ Yellow │ 8     │\n'
            '│ Cherry     │ 7         │ 31        │ Red    │ 92    │\n'
            '│ Kiwi       │ 4         │ 102       │ Green  │ 1     │\n'
            '│ Strawberry │ 6         │ 134       │ Red    │ 28    │\n'
            '└────────────┴───────────┴───────────┴────────┴───────┘',
        )
        for case, expect in zip(cases, expected):
            self.assertEqual(make_table(**vars(case)), expect, msg="Failed when creating labels.")

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

        expected = (
            '┌───────┬───────────┬───────────┐\n'
            '│ Fruit │ Tastiness │ Sweetness │\n'
            '├───────┼───────────┼───────────┤\n'
            '│ Apple │     5     │    70     │\n'
            '└───────┴───────────┴───────────┘',

            '┌────────┬───────────┬───────────┬────────┐\n'
            '│ Fruit  │ Tastiness │ Sweetness │ Colour │\n'
            '├────────┼───────────┼───────────┼────────┤\n'
            '│ Apple  │     5     │    70     │  Red   │\n'
            '│ Banana │     3     │     5     │ Yellow │\n'
            '│ Cherry │     7     │    31     │  Red   │\n'
            '└────────┴───────────┴───────────┴────────┘',

            '┌────────────┬───────────┬───────────┬────────┬───────┐\n'
            '│   Fruit    │ Tastiness │ Sweetness │ Colour │ Smell │\n'
            '├────────────┼───────────┼───────────┼────────┼───────┤\n'
            '│   Apple    │     5     │    70     │  Red   │  76   │\n'
            '│   Banana   │     3     │     5     │ Yellow │   8   │\n'
            '│   Cherry   │     7     │    31     │  Red   │  92   │\n'
            '│    Kiwi    │     4     │    102    │ Green  │   1   │\n'
            '│ Strawberry │     6     │    134    │  Red   │  28   │\n'
            '└────────────┴───────────┴───────────┴────────┴───────┘'
        )

        for case, expect in zip(cases, expected):
            self.assertEqual(make_table(**vars(case)), expect, msg="Failed when using align_center parameter.")

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

        expected = (
            '┌───────────────────────────────────────────────┐\n'
            '│            My Favourite Long Words            │\n'
            '├───────────────────────────────────────────────┤\n'
            '│ Pneumonoultramicroscopicsilicovolcanoconiosis │\n'
            '│     Hippopotomonstrosesquippedaliophobia      │\n'
            '│      Supercalifragilisticexpialidocious       │\n'
            '│        Pseudopseudohypoparathyroidism         │\n'
            '│         Floccinaucinihilipilification         │\n'
            '│         Antidisestablishmentarianism          │\n'
            '│                       .                       │\n'
            '└───────────────────────────────────────────────┘',

            '┌───────────────────────────────────────────────┐\n'
            '│ My Favourite Long Words                       │\n'
            '├───────────────────────────────────────────────┤\n'
            '│ Pneumonoultramicroscopicsilicovolcanoconiosis │\n'
            '│ Hippopotomonstrosesquippedaliophobia          │\n'
            '│ Supercalifragilisticexpialidocious            │\n'
            '│ Pseudopseudohypoparathyroidism                │\n'
            '│ Floccinaucinihilipilification                 │\n'
            '│ Antidisestablishmentarianism                  │\n'
            '│ .                                             │\n'
            '└───────────────────────────────────────────────┘',

            '┌───────────────────────────────────────────────┐\n'
            '│                   Alphabet                    │\n'
            '├───────────────────────────────────────────────┤\n'
            '│                       A                       │\n'
            '│                       B                       │\n'
            '│                       C                       │\n'
            '│                       D                       │\n'
            '│                       E                       │\n'
            '│                       F                       │\n'
            '│ Pneumonoultramicroscopicsilicovolcanoconiosis │\n'
            '└───────────────────────────────────────────────┘',

            '┌───────────────────────────────────────────────┐\n'
            '│ Alphabet                                      │\n'
            '├───────────────────────────────────────────────┤\n'
            '│ A                                             │\n'
            '│ B                                             │\n'
            '│ C                                             │\n'
            '│ D                                             │\n'
            '│ E                                             │\n'
            '│ F                                             │\n'
            '│ Pneumonoultramicroscopicsilicovolcanoconiosis │\n'
            '└───────────────────────────────────────────────┘',
        )

        for case, expect in zip(cases, expected):
            self.assertEqual(make_table(**vars(case)), expect,
                             msg="Columns did not seem to scale in size appropriately.")

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

        expected = (
            '┌──────┬──────┬─────┬──────┬──────┬─────┐\n'
            '│  3   │ None │ 12  │  A   │ 12.6 │ 12j │\n'
            '├──────┼──────┼─────┼──────┼──────┼─────┤\n'
            '│ None │  1   │ 2.5 │ None │ 32j  │ 123 │\n'
            '└──────┴──────┴─────┴──────┴──────┴─────┘',
        )

        for case, expect in zip(cases, expected):
            self.assertEqual(
                make_table(**vars(case)),
                expect,
                "Could not handle list of object that implement __str__() correctly. "
            )

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

        expected = (
            '┌───────┬───────────┬───────────┐\n'
            '│ Fruit │ Tastiness │ Sweetness │\n'
            '├───────┼───────────┼───────────┤\n'
            '│ Apple │     5     │    70     │\n'
            '└───────┴───────────┴───────────┘',
            '┌────────┬───────────┬───────────┬────────┐\n'
            '│ Fruit  │ Tastiness │ Sweetness │ Colour │\n'
            '├────────┼───────────┼───────────┼────────┤\n'
            '│ Apple  │     5     │    70     │  Red   │\n'
            '│ Banana │     3     │     5     │ Yellow │\n'
            '│ Cherry │     7     │    31     │  Red   │\n'
            '└────────┴───────────┴───────────┴────────┘',
            '┌────────────┬───────────┬───────────┬────────┬───────┐\n'
            '│   Fruit    │ Tastiness │ Sweetness │ Colour │ Smell │\n'
            '├────────────┼───────────┼───────────┼────────┼───────┤\n'
            '│   Apple    │     5     │    70     │  Red   │  76   │\n'
            '│   Banana   │     3     │     5     │ Yellow │   8   │\n'
            '│   Cherry   │     7     │    31     │  Red   │  92   │\n'
            '│    Kiwi    │     4     │    102    │ Green  │   1   │\n'
            '│ Strawberry │     6     │    134    │  Red   │  28   │\n'
            '└────────────┴───────────┴───────────┴────────┴───────┘',
        )

        for case, expect in zip(cases, expected):
            self.assertEqual(
                make_table(**vars(case)),
                expect,
                msg="Couldn't handle a class with a __str__ implementation."
            )

    def test_010_lots_of_rows(self) -> None:
        rows = [["Just", "Another", "Row"] for _ in range(25)]

        expected_1 = (
            '┌──────┬─────────┬─────┐\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '└──────┴─────────┴─────┘'
        )
        expected_2 = (
            '┌──────┬─────────┬─────┐\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '└──────┴─────────┴─────┘'
        )
        self.assertEqual(make_table(rows), expected_1, msg="Couldn't handle lots of rows.")
        self.assertEqual(make_table(rows, centered=True), expected_2, msg="Couldn't handle lots of rows.")

    def test_011_lots_of_columns(self) -> None:
        rows = [["Just", "Another", "Column"] * 4 for _ in range(25)]

        expected_1 = (
            '┌──────┬─────────┬────────┬──────┬─────────┬────────┬──────┬─────────┬────────┬──────┬─────────┬────────┐\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '└──────┴─────────┴────────┴──────┴─────────┴────────┴──────┴─────────┴────────┴──────┴─────────┴────────┘'
        )

        expected_2 = (
            '┌──────┬─────────┬────────┬──────┬─────────┬────────┬──────┬─────────┬────────┬──────┬─────────┬────────┐\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '└──────┴─────────┴────────┴──────┴─────────┴────────┴──────┴─────────┴────────┴──────┴─────────┴────────┘'
        )

        self.assertEqual(make_table(rows), expected_1, msg="Couldn't handle lots of cols.")
        self.assertEqual(make_table(rows, centered=True), expected_2, msg="Couldn't handle lots of cols.")
