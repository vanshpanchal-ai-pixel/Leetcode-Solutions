# LeetCode 217 — Contains Duplicate

**Difficulty:** Easy  
**Topics:** Array, Hash Set  
**Language:** Python  
**Status:** Solved ✅

## Problem Statement

Given an integer array `nums`, return `True` if any value appears at least twice in the array, and return `False` if every element is distinct.

### Example 1

**Input:**
```python
nums = [1, 2, 3, 1]
```

**Output:**
```python
True
```

**Explanation:** The element `1` appears twice.

### Example 2

**Input:**
```python
nums = [1, 2, 3, 4]
```

**Output:**
```python
False
```

**Explanation:** Every element is distinct.

---

## Approach 1 — Using a List (Initial Approach)

Maintain a list called `seen` to store previously encountered elements.

For every number:
1. Check whether it already exists in `seen`.
2. If it exists, return `True`.
3. Otherwise, append it to `seen`.
4. If the loop finishes, return `False`.

### Complexity Analysis

- **Time Complexity:** O(n²) worst case — list membership checking takes O(n).
- **Space Complexity:** O(n) — storing previously encountered elements.

---

## Approach 2 — Using a Set (Optimized Approach)

Use Python's built-in `set()` data structure instead of a list.

Sets use hashing, which provides average O(1) lookup and insertion.

### Python Solution

```python
class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False
```

### Complexity Analysis

| Complexity | Value | Explanation |
|---|---|---|
| Time | O(n) average | Set lookup and insertion are O(1) average |
| Space | O(n) | Set may store up to n distinct elements |

---

## Key Learnings

- Difference between Python Lists and Sets.
- Understanding hashing and efficient lookups.
- Optimizing time complexity from O(n²) to O(n) average.
- Understanding `return` versus `break`.
- Correct placement of return statements inside and outside loops.
- Writing clean and optimized Python code.

## Conclusion

This problem helped me understand how choosing the right data structure can significantly improve algorithm efficiency.

**Key takeaway:** Always consider whether a Hash Set can replace repeated linear searches when checking for duplicates.

---

**Problem:** [LeetCode 217 — Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
