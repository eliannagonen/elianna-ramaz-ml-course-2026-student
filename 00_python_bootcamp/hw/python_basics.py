"""HW00 — Python Bootcamp: Implementation

Complete the functions below. Each function has a docstring describing
what it should do, along with examples. Run `uv run pytest` to check
your work, and `uv run python score.py` to see your current grade.
"""

from __future__ import annotations

from typing import Callable

# ── Part 1: Lists ─────────────────────────────────────────────────────────────


def flatten(nested: list[list]) -> list:
    """Return a single flat list from a list of lists.

    Examples:
        >>> flatten([[1, 2], [3, 4], [5]])
        [1, 2, 3, 4, 5]
        >>> flatten([[], [1]])
        [1]
        >>> flatten([])
        []
    """

    result = []
    
    for sublist in nested:
        for item in sublist:
            result.append(item)

    return result


def most_frequent(items: list) -> object:
    """Return the element that appears most often in items.

    If there is a tie, returning any one of the tied elements is fine.
    Raise ValueError if items is empty.

    Examples:
        >>> most_frequent([1, 2, 2, 3])
        2
        >>> most_frequent(['a', 'b', 'a', 'c', 'a'])
        'a'
    """
    if len(items) == 0:
        raise ValueError("Items is empty")

    best_item = items[0]
    best_count = 0

    for item in items:
        if items.count(item) > best_count:
            best_item = item
            best_count = items.count(item)

    return best_item


def running_average(numbers: list[float]) -> list[float]:
    """Return the cumulative average at each position.

    The i-th element of the result is the mean of numbers[0], ..., numbers[i].

    Examples:
        >>> running_average([10.0, 20.0, 30.0])
        [10.0, 15.0, 20.0]
        >>> running_average([4.0])
        [4.0]
        >>> running_average([])
        []
    """
    total = 0
    count = 0
    averages = []

    for number in numbers:
        total += number
        count += 1
        averages.append(total / count)

    return averages


def chunk(items: list, size: int) -> list[list]:
    """Split items into sublists of length size.

    The last sublist may be shorter if len(items) is not divisible by size.

    Examples:
        >>> chunk([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
        >>> chunk([1, 2, 3], 3)
        [[1, 2, 3]]
        >>> chunk([], 4)
        []
    """

    result = []

    for i in range(0, len(items), size):
        result.append(items[i : i + size])

    return result


def rotate(items: list, k: int) -> list:
    """Rotate items left by k positions.

    A negative k rotates right. If items is empty, return [].
    k larger than len(items) wraps around correctly.

    Examples:
        >>> rotate([1, 2, 3, 4, 5], 2)
        [3, 4, 5, 1, 2]
        >>> rotate([1, 2, 3], -1)
        [3, 1, 2]
        >>> rotate([1, 2, 3], 4)
        [2, 3, 1]
    """
    if len(items) == 0:
        return items

    k = k % len(items)
    return items[k:] + items[:k]


def run_length_encode(items: list) -> list[tuple]:
    """Compress consecutive identical elements into (count, value) tuples.

    Examples:
        >>> run_length_encode(['a', 'a', 'b', 'b', 'b', 'a'])
        [(2, 'a'), (3, 'b'), (1, 'a')]
        >>> run_length_encode([1, 2, 3])
        [(1, 1), (1, 2), (1, 3)]
        >>> run_length_encode([])
        []
    """
    if len(items) == 0:
        return []

    count = 0
    current_item = items[0]
    item_groups = []

    for item in items:
        if item == current_item:
            count += 1
        else:
            item_groups.append((count, current_item))
            count = 1
            current_item = item

    item_groups.append((count, current_item))
    return item_groups


def sliding_window(items: list, size: int) -> list[list]:
    """Return all consecutive windows of length size.

    Each window overlaps with the previous one by size-1 elements.
    If len(items) < size, return [].

    Examples:
        >>> sliding_window([1, 2, 3, 4, 5], 3)
        [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        >>> sliding_window([1, 2, 3], 2)
        [[1, 2], [2, 3]]
        >>> sliding_window([1, 2], 3)
        []
        >>> sliding_window([], 2)
        []
    """
    conseq_windows = []

    if len(items) < size:
        return []

    for i in range(len(items) - size + 1):
        conseq_windows.append(items[i :size + i])

    return conseq_windows


# ── Part 2: Dictionaries ──────────────────────────────────────────────────────


def count_occurrences(items: list) -> dict:
    """Return a dict mapping each unique element to its count in items.

    Examples:
        >>> count_occurrences(['a', 'b', 'a', 'c', 'b', 'b'])
        {'a': 2, 'b': 3, 'c': 1}
        >>> count_occurrences([])
        {}
    """

    count_items = {}

    for element in items:
        if element not in count_items:
            count_items[element] = 1
        else:
            count_items[element] += 1

    return count_items


def invert_dict(d: dict) -> dict:
    """Return a new dict with keys and values swapped.

    Examples:
        >>> invert_dict({'a': 1, 'b': 2})
        {1: 'a', 2: 'b'}
    """

    new_dict = {}
    for key, value in d.items():
        new_dict[value] = key

    return new_dict

def group_by(items: list[dict], key: str) -> dict[str, list[dict]]:
    """Group a list of dicts by the value at the given key.

    Examples:
        >>> records = [
        ...     {'name': 'Alice', 'dept': 'Eng'},
        ...     {'name': 'Bob', 'dept': 'HR'},
        ...     {'name': 'Carol', 'dept': 'Eng'},
        ... ]
        >>> result = group_by(records, 'dept')
        >>> len(result['Eng'])
        2
        >>> len(result['HR'])
        1
    """
    final_dict = {}

    for record in items:
        group_value = record[key]

        if group_value not in final_dict:
            final_dict[group_value] = []
        
        final_dict[group_value].append(record)

    return final_dict
            

def deep_get(d: dict, path: str, default: object = None) -> object:
    """Retrieve a value from a nested dict using a dot-separated key path.

    Return default if any key along the path is missing.

    Examples:
        >>> deep_get({'a': {'b': {'c': 42}}}, 'a.b.c')
        42
        >>> deep_get({'a': 1}, 'a.b', default=-1)
        -1
        >>> deep_get({'x': 10}, 'y')  # returns None (default)
    """

    keys = path.split('.')

    current = d
    for key in keys:
        if not isinstance(current, dict):
            return default
        
        if key not in current:
            return default
        else:
            current = current[key]

    return current
        

def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """Return indices (i, j) where nums[i] + nums[j] == target, with i < j.

    ReturnNone if no such pair exists.

    Hint: There is an elegant O(n) solution using a dict. As you scan through
    nums, ask: "have I already seen the number I need to pair with this one?"

    Examples:
        >>> two_sum([2, 7, 11, 15], 9)
        (0, 1)
        >>> two_sum([3, 2, 4], 6)
        (1, 2)
        >>> two_sum([1, 2, 3], 100)
        None
    """

    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        else:
            seen[num] = i

    return None

# ── Part 3: Sets ──────────────────────────────────────────────────────────────


def find_duplicates(items: list) -> set:
    """Return the set of elements that appear more than once in items.

    Examples:
        >>> find_duplicates([1, 2, 2, 3, 3, 3, 4])
        {2, 3}
        >>> find_duplicates([1, 2, 3])
        set()
        >>> find_duplicates([])
        set()
    """
    duplicates = set()
    seen = set()

    for element in items:
        if element in seen:
            duplicates.add(element)
        else:
            seen.add(element)

    return duplicates


def jaccard_similarity(a: set, b: set) -> float:
    """Return |A intersection B| / |A union B|.

    Return 0.0 if both sets are empty.

    Examples:
        >>> jaccard_similarity({1, 2, 3}, {2, 3, 4})
        0.5
        >>> jaccard_similarity({1, 2}, {3, 4})
        0.0
        >>> jaccard_similarity(set(), set())
        0.0
    """

    union = a | b
    intersection = a & b

    if len(union) == 0:
        return 0.0

    return len(intersection) / len(union)

# ── Part 4: Higher-order functions ────────────────────────────────────────────


def apply_twice(f: Callable, x: object) -> object:
    """Apply f to x, then apply f to the result: f(f(x)).

    Examples:
        >>> apply_twice(lambda n: n * 2, 3)
        12
        >>> apply_twice(str.upper, 'hello')
        'HELLO'
    """

    return f(f(x))


def make_multiplier(n: float) -> Callable[[float], float]:
    """Return a function that multiplies its argument by n.

    Each call to make_multiplier returns an independent function.

    Examples:
        >>> double = make_multiplier(2)
        >>> double(5)
        10.0
        >>> triple = make_multiplier(3)
        >>> triple(4)
        12.0
    """

    def multiplier(x):
        return x * n

    return multiplier

def pipeline(*funcs: Callable) -> Callable:
    """Return a single function that applies each func in sequence (left to right).

    pipeline(f, g, h)(x) is equivalent to h(g(f(x))).
    If no functions are provided, the returned function is the identity: f(x) == x.

    Examples:
        >>> add1 = lambda x: x + 1
        >>> double = lambda x: x * 2
        >>> pipeline(add1, double)(3)
        8
        >>> pipeline()(42)
        42
    """

    def apply_funcs(x):
        if len(funcs) == 0:
            return x
        result = x
        for func in funcs:
            result = func(result)
        return result

    return apply_funcs


def memoize(f: Callable) -> Callable:
    """Return a version of f that caches results by argument.

    Calling the memoized function with the same argument a second time
    must return the cached result WITHOUT calling f again.

    Use a closure over a dict to store previously computed results.

    Examples:
        >>> call_count = 0
        >>> def tracked(x):
        ...     global call_count
        ...     call_count += 1
        ...     return x ** 2
        >>> cached = memoize(tracked)
        >>> cached(4)
        16
        >>> cached(4)   # should not increment call_count
        16
    """

    cache = {}

    def cached_f(x):
        if x in cache:
            return cache[x]
        else:
            cache[x] = f(x)
            return cache[x]

    return cached_f



# ── Part 5: Classes ───────────────────────────────────────────────────────────


class Student:
    """A student with a name and a list of grades (0-100).

    Supports comparison via average grade, enabling natural sorting.
    """

    def __init__(self, name: str, grades: list[float]) -> None:
        self.name = name
        self.grades = grades

    def average(self) -> float:
        """Return the mean of all grades. Returns 0.0 if grades is empty."""
        if len(self.grades) == 0:
            return 0.0
        else:
            return sum(self.grades) / len(self.grades)

    def highest(self) -> float:
        """Return the highest grade. Returns 0.0 if grades is empty."""
        if len(self.grades) == 0:
            return 0.0
        else:
            return max(self.grades)

    def letter_grade(self) -> str:
        """Return the letter grade for this student's average.

        Boundaries: A >= 90, B >= 80, C >= 70, D >= 60, F otherwise.
        """
        avg = self.average()

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def __repr__(self) -> str:
        """Return a string like: Student('Alice', avg=88.5)"""
        avg = self.average()

        return f"Student('{self.name}', avg={avg:.1f})"

    def __lt__(self, other: "Student") -> bool:
        """Compare students by average grade (enables sorted() and min/max)."""
        return self.average() < other.average()



class Gradebook:
    """Manages a collection of students, keyed by name."""

    def __init__(self) -> None:
        self.students: dict[str, Student] = {}

    def add_student(self, student: Student) -> None:
        """Add a student to the gradebook.

        Raises ValueError if a student with the same name already exists.
        """
        if student.name in self.students:
            raise ValueError()
        else:
            self.students[student.name] = student
        

    def top_students(self, n: int) -> list[Student]:
        """Return the n students with the highest averages, in descending order."""
        all_sorted = sorted(self.students.values(), reverse = True)
        return all_sorted[:n]

    def class_average(self) -> float:
        """Return the mean of all student averages. Returns 0.0 if empty."""

        all_averages = [student.average() for student in self.students.values()]

        if len(self.students) == 0:
            return 0.0
        else:
            return sum(all_averages)/len(all_averages)
 