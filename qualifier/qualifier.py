from typing import Any, List, Optional


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """

    # declare variables for use
    table = []
    has_labels: bool = True
    max_width: List[int] = []

    # Check if labels were provided
    if (labels is None):

        has_labels = False


    # If labels weren't provided
    if not has_labels:

        # find the max width of the single 
        max_width.append(len(max(rows)[0]))

    # if labels were provided
    else:
        
        curr_max: int

        # find the max of each column
        for item_index in range(len(labels)):
            
            curr_max = len(rows[0][item_index])

            for sub_index in range(len(rows)):

                curr_max = max(curr_max, len(rows[sub_index][item_index]))
                
            # end for
            
            max_width.append(curr_max)

        # end for

    entire_width = sum(max_width)

    if not has_labels:

        # print the one column
        table.append("" + chr(9484) + chr(9472) * (entire_width + 2) + chr(9488))

        # check if centered
        if not centered:

            for row in rows:
                table.append("" + chr(9474) + " " + row[0] + " " * (entire_width - len(row[0]) + 1) + chr(9474))
        
        # if centered
        else:

            for row in rows:

                leading_space = ((entire_width - len(row[0])) // 2 + 1)

                if not entire_width & 1:

                    table.append("" + chr(9474) + " " * leading_space + row[0]
                        + " " * leading_space + chr(9474))

                else:

                    table.append("" + chr(9474) + " " * leading_space + row[0]
                        + " " * (leading_space + bool(leading_space & 1 and len(row[0]) < entire_width)) + chr(9474))

        
        table.append("" + chr(9492) + (chr(9472) * (entire_width + 2)) + chr(9496))

    # if there are multiple columns
    else:

        num_of_cross = len(labels) - 1

        top = "" + chr(9484)

        label_section = "" + chr(9474)

        middle = "" + chr(9500)

        bottom = "" + chr(9492)



        # if the table is centered
        if centered:

            for i in range(num_of_cross):

                top += "" + (max_width[i] + 2) * chr(9472) + chr(9516)
                
                leading_space = ((max_width[i] - len(labels[i])) // 2 + 1)
                do_add_one = bool(leading_space & 1 and len(labels(i)) < max_width[i])
                label_section += " " * (leading_space) + labels[i] + " " * (leading_space + do_add_one) + chr(9474)

                middle += "" + (max_width[i] + 2) * chr(9472) + chr(9532)

                bottom += "" + (max_width[i] + 2) * chr(9472) + chr(9524)

            leading_space = ((max_width[-1] - len(labels[-1])) // 2 + 1)
            do_add_one = bool(leading_space & 1 and len(labels(-1)) < max_width[-1])

            table.append("" + top + (max_width[-1] + 2) * chr(9472) + chr(9488))
            table.append("" + label_section + " " * (leading_space) + labels[-1] + (leading_space + do_add_one) * " " + chr(9474))
            table.append("" + middle + (max_width[-1] + 2) * chr(9472) + chr(9508))

            for row in rows:

                curr_line = "" + chr(9474)

                for index, col in enumerate(row):

                    leading_space = ((max_width[index] - len(col)) // 2 + 1)

                    if not max_width[index] & 1:

                        curr_line += (" " * leading_space) + col + (" " * leading_space) + chr(9474)

                    else:

                        do_add_one = bool(leading_space & 1 and len(col) < max_width[index])

                        curr_line += (" " * leading_space) + col + (" " * (leading_space + do_add_one)) + chr(9474)


                table.append(curr_line)

            table.append("" + bottom + chr(9472) * (max_width[-1] + 2) + chr(9496))

        # if table is not centered
        else:

            for i in range(num_of_cross):

                top += "" + (max_width[i] + 2) * chr(9472) + chr(9516)
                
                label_section += " " + labels[i] + " " * (max_width[i] - len(labels) + 2) + chr(9474)

                middle += "" + (max_width[i] + 2) * chr(9472) + chr(9532)

                bottom += "" + (max_width[i] + 2) * chr(9472) + chr(9524)

            table.append("" + top + (max_width[-1] + 2) * chr(9472) + chr(9488))
            table.append("" + label_section + " " + labels[-1] + (max_width[-1] - len(labels[-1]) + 1) * " " + chr(9474))
            table.append("" + middle + (max_width[-1] + 2) * chr(9472) + chr(9508))

            for row in rows:

                curr_line = "" + chr(9474)

                for index, col in enumerate(row):

                    curr_line += " " + col + " " * (max_width[index] - len(row[0]) + 1) + chr(9474)
                
                table.append(curr_line)

            table.append("" + bottom + chr(9472) * (max_width[-1] + 2) + chr(9496))

    return "\n".join(table)

