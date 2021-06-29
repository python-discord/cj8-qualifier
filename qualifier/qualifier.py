from typing import Any, List, Optional


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    
    table = []

    max_len: List[int] = []

    # check the maximum width for each column
    for index in range(len(rows[0])):

        curr_max: int = max([len(str(rows[curr][index])) for curr in range(len(rows))])

        if labels:

            curr_max = max(curr_max, len(str(labels[index])))
        
        max_len.append(curr_max)


    # print header 
    if labels:

        sep = [""] * ((len(labels) if (len(labels) > 1) else 1) + 1)

        # print top section
        if (len(sep) > 2):

            sep[0] = "" + chr(9484)
            sep[1] = "" + chr(9516)
            sep[2] = "" + chr(9488)

        else:

            sep[0] = "" + chr(9484)
            sep[1] = "" + chr(9488)

        table.append(create_table_row(sep, ["" + chr(9472) for _ in range(len(labels))], max_len, padding="" + chr(9472), is_centered=centered))
        
        # print middle section
        table.append(create_table_row(["" + chr(9474), "" + chr(9474)], labels, max_len, is_centered=centered))
        
        # print Bottom section
        if (len(sep) > 2):

            sep[0] = "" + chr(9500)
            sep[1] = "" + chr(9532)
            sep[2] = "" + chr(9508)

        else:

            sep[0] = "" + chr(9500)
            sep[1] = "" + chr(9508)
        
        table.append(create_table_row(sep, ["" + chr(9472) for _ in range(len(labels))], max_len, padding="" + chr(9472), is_centered=centered))

    # if there are no labels
    else:

        # print top-most part
        sep = [""] * ((len(rows[0]) if (len(rows[0]) > 1) else 1) + 1)

        if (len(sep) > 2):

            sep[0] = "" + chr(9484)
            sep[1] = "" + chr(9516)
            sep[2] = "" + chr(9488)

        else:

            sep[0] = "" + chr(9484)
            sep[1] = "" + chr(9488)

        table.append(create_table_row(sep, ["" + chr(9472) for _ in range(len(rows[0]))], max_len, padding="" + chr(9472), is_centered=centered))
    
    # Create the middle
    for words in rows:

        table.append(create_table_row(["" + chr(9474) for _ in range(2)], words, max_len, is_centered=centered))

    # Create the bottom
    sep = [""] * ((len(rows[0]) if (len(rows[0]) > 1) else 1) + 1)
        
    if (len(sep) > 2):

        sep[0] = "" + chr(9492)
        sep[1] = "" + chr(9524)
        sep[2] = "" + chr(9496)

    else:

        sep[0] = "" + chr(9492)
        sep[1] = "" + chr(9496)
    

    table.append(create_table_row(sep, ["" + chr(9472) for _ in range(len(rows[0]))], max_len, padding="" + chr(9472), is_centered=centered))
    
    return "\n".join(table)

def create_table_row(separator: List[str], words: List[str], max_len: List[int], padding: Optional[str] = " ", is_centered: bool = False) -> str:

    table_row = []

    for index, word in enumerate(words):
    
        table_group = str(word)

        if (is_centered):

            if (len(str(word)) & 1 != max_len[index] & 1):

                table_group += padding

            while (len(table_group) - 2 < max_len[index]):

                table_group = padding + table_group + padding
            
        else:

            table_group = padding + table_group

            while (len(table_group) - 2 < max_len[index]):

                table_group += padding

        
        if index == 0:

            table_group = separator[0] + table_group + separator[1]

        elif index < len(words) - 1 and len(separator) > 2:

            table_group += separator[1]
            
        elif len(separator) > 2:

            table_group += separator[2]

        else:

            table_group += separator[1]


        table_row.append(table_group)

    return "".join(table_row)