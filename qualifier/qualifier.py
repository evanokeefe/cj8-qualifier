from typing import Any, List, Optional
from collections import defaultdict

def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """

    if labels is not None:
        rows = [labels] + rows

    lengths = defaultdict(int)
    for row in rows:
        for idx, col in enumerate(row):
            col = str(col)
            if len(col) > lengths[idx]:
                lengths[idx] = len(col)

    width = ['─' * (n + 2) for n in lengths.values()]
    output = [f"┌{'┬'.join(width)}┐"]
    for num, row in enumerate(rows):
        if labels and num == 1:
            output.append(f"├{'┼'.join(width)}┤")
        if centered:
            line = [str(col).center(lengths[idx], " ") for idx, col in enumerate(row)]
        else:
            line = [str(col).ljust(lengths[idx], " ") for idx, col in enumerate(row)]
        output.append(f"│ {' │ '.join(line)} │")
    output.append(f"└{'┴'.join(width)}┘")
    return "\n".join(output)
