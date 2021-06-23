# Summer Code Jam 2021: Qualifier

To qualify for the upcoming Summer Code Jam, you'll have to complete a qualifier assignment. In this assignment you have
been tasked to create a function that makes a table with columns and rows.

Please read the instructions carefully and submit your solution before the deadline using the
[sign-up form](https://form.jotform.com/211714357615050).

# Table of Contents

- [Qualifying for the Code Jam](#qualifying-for-the-code-jam)
- [Rules and Guidelines](#rules-and-guidelines)
- [Qualifier Assignment](#qualifier-assignment)
  - [Function Signature](#function-signature)
  - [Examples](#examples)
    - [Example 1](#example-1)
    - [Example 2](#example-2)
    - [Example 3](#example-3)

# Qualifying for the Code Jam

To qualify for the Code Jam you will be required to upload your submission to the [sign-up form](https://form.jotform.com/211714357615050).
We set up our test suite so you don't have to worry about setting one up yourself.

Your code will be tested with a multitude of tests to test all aspects of your code making sure it works.

# Rules and Guidelines

- Your submission will be tested using a Python 3.9.5 interpreter without any additional packages installed. You're allowed to use everything included in Python's standard library, but nothing else. Please make sure to include the relevant `import` statements in your submission.

- Use [`qualifier.py`](qualifier/qualifier.py) as the base for your solution. It includes a stub for the function you need to write: `make_table`.

- Do not change the **signature** of the function included in [`qualifier.py`](qualifier/qualifier.py). The test suite we will use to judge your submission relies on it. Everything else, including the docstring, may be changed.

- Do not include "debug" code in your submission. You should remove all debug prints and other debug statements before you submit your solution.

- This qualifier task is supposed to be **an individual challenge**. You should not discuss (parts of) your solution in public (including our server), or rely on others' solutions to the qualifier. Failure to meet this requirement may result in the **disqualification** of all parties involved. You are still allowed to do research and ask questions about Python as they relate to your qualifier solution, but try to use general examples if you post code along with your questions.


# Qualifier Assignment

For the qualifier, you are required to write a function that creates and returns an ascii table.
Your table must use these characters for the border. `│ ─ ┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘`
  - Length of each row will always equal the length of labels (if labels are provided) for the input data
  - No item in any row will contain an escape character such as `\n` for the input data
  - If an item cannot be centered evenly, the extra space character can be placed on either side.
  - Each column should be made wide enough to fit the longest item, with one space on either side for padding

### Function Signature
```py
def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    ...
```
## Examples

### Example 1

This example shows the function being used to create a single column table. Each column should be made wide enough
to fit the longest item with one space either side.

```py
table = make_table(
    rows=[
        ["Lemon"],
        ["Sebastiaan"],
        ["KutieKatj9"],
        ["Jake"],
        ["Not Joe"]
    ]
)
>>> print(table)
┌────────────┐
│ Lemon      │
│ Sebastiaan │
│ KutieKatj9 │
│ Jake       │
│ Not Joe    │
└────────────┘
```

### Example 2

This example shows a table with three columns, each column is wide enough to fit the largest item of column with a
space either side. The labels are placed independently at the top of each column to give them a clearer meaning.

```py
table = make_table(
    rows=[
        ["Lemon", 18_3285, "Owner"],
        ["Sebastiaan", 18_3285.1, "Owner"],
        ["KutieKatj", 15_000, "Admin"],
        ["Jake", "MoreThanU", "Helper"],
        ["Joe", -12, "Idk Tbh"]
    ],
    labels=["User", "Messages", "Role"]
)
>>> print(table)
┌────────────┬───────────┬─────────┐
│ User       │ Messages  │ Role    │
├────────────┼───────────┼─────────┤
│ Lemon      │ 183285    │ Owner   │
│ Sebastiaan │ 183285.1  │ Owner   │
│ KutieKatj  │ 15000     │ Admin   │
│ Jake       │ MoreThanU │ Helper  │
│ Joe        │ -12       │ Idk Tbh │
└────────────┴───────────┴─────────┘
```

### Example 3

This example shows the usage of centered. Each item will be aligned within the center of the column. Remember that the
labels are also aligned.

```py
table = make_table(
   rows=[
       ["Ducky Yellow", 3],
       ["Ducky Dave", 12],
       ["Ducky Tube", 7],
       ["Ducky Lemon", 1]
   ],
   labels=["Name", "Duckiness"],
   centered=True
)
>>> print(table)
┌──────────────┬───────────┐
│     Name     │ Duckiness │
├──────────────┼───────────┤
│ Ducky Yellow │     3     │
│  Ducky Dave  │    12     │
│  Ducky Tube  │     7     │
│ Ducky Lemon  │     1     │
└──────────────┴───────────┘
```

## Good Luck!

![Event Banner](https://github.com/python-discord/branding/blob/main/jams/summer_code_jam_2021/site_banner.png?raw=true)
