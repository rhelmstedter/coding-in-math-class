from functools import reduce
from operator import mul

from rich.console import Console
from rich.table import Table


def _partition(target, partition_size):
    units = tuple(1 for i in range(target))
    for i in range(0, target, partition_size):
        yield sum(units[i : i + partition_size])


def max_product(target):
    partitions = (tuple(_partition(target, p_size)) for p_size in range(1, target))
    partitions_with_products = [(p, reduce(mul, p)) for p in partitions]
    return max(partitions_with_products, key=lambda x: x[1])


console = Console()
table = Table(title="Split It")
table.add_column("[green]Number", justify="center")
table.add_column("[green]Optimal Partition", justify="left")
table.add_column("[green]Product", justify="right")

for target in range(2, 26):
    mp = max_product(target)
    table.add_row(f"[blue]{target}", f"{', '.join(map(str, mp[0]))}", f"[blue]{mp[1]}")
console.print(table)
