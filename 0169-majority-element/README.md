# 0169. Majority Element

**Difficulty:** Easy  
**Topics:** Array, Hash Table, Divide and Conquer, Sorting, Boyer-Moore Voting Algorithm  
**Language:** Python

## Problem

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `⌊n / 2⌋` times.

It is guaranteed that a majority element always exists.

### Example

```python
Input: nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2
```

## Approach 1: Hash Map (Frequency Counting)

The first approach uses a Python dictionary to count the frequency of every element.

### Logic

1. Create an empty dictionary `freq`.
2. Traverse the array.
3. Count each element using `freq.get(num, 0) + 1`.
4. Calculate the majority threshold using `len(nums) // 2`.
5. Return the element whose frequency is greater than the threshold.

### Python Code

```python
class Solution(object):
    def majorityElement(self, nums):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        threshold = len(nums) // 2

        for key, value in freq.items():
            if value > threshold:
                return key
```

### Complexity Analysis

- **Time Complexity:** O(n) – Two traversals of the array.
- **Space Complexity:** O(n) – Dictionary stores element frequencies.

---

## Approach 2: Boyer-Moore Voting Algorithm (Optimized)

**This is the optimal approach**, achieving linear time complexity and constant auxiliary space.

### Intuition

The Boyer-Moore Voting Algorithm works on the concept of cancellation.

Imagine every occurrence of a different element cancels one occurrence of the current candidate.

Since the majority element appears more than half the time, it cannot be completely cancelled by all other elements combined.

Therefore, the majority element will remain as the final candidate.

### Algorithm

We maintain two variables:

- `candidate`: Stores the current majority candidate.
- `count`: Tracks the candidate's voting balance.

**Three rules:**

1. If `count == 0`, select the current element as the new candidate and increase count.
2. If the current element equals the candidate, increment count.
3. Otherwise, decrement count.

After processing the entire array, the candidate is the majority element.

### Python Solution

```python
class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count += 1

            elif num == candidate:
                count += 1

            else:
                count -= 1

        return candidate
```

### Dry Run

Input:

```python
nums = [3, 3, 4, 3, 4, 3, 3]
```

Initial values:

```python
candidate = None
count = 0
```

| Step | Number | Action | Candidate | Count |
|---|---|---|---|---|
| 1 | 3 | New candidate | 3 | 1 |
| 2 | 3 | Increment | 3 | 2 |
| 3 | 4 | Decrement | 3 | 1 |
| 4 | 3 | Increment | 3 | 2 |
| 5 | 4 | Decrement | 3 | 1 |
| 6 | 3 | Increment | 3 | 2 |
| 7 | 3 | Increment | 3 | 3 |

Final result:

```python
Output: 3
```

The majority element survives the cancellation process.

### Complexity Analysis

- **Time Complexity:** O(n) – Only one traversal of the array.
- **Auxiliary Space Complexity:** O(1) – Uses only two variables, regardless of input size.

---

## Comparison of Both Approaches

| Approach | Time Complexity | Space Complexity |
|---|---|---|
| Hash Map | O(n) | O(n) |
| Boyer-Moore Voting | O(n) | O(1) |

## Key Learnings

- Learned frequency counting using Python dictionaries.
- Understood the concept of cancellation in Boyer-Moore Voting.
- Practiced tracking a candidate and its voting balance.
- Optimized an O(n) extra-space solution to O(1) auxiliary space.
- Understood how majority elements can survive pairwise cancellation.

**Final Takeaway:** When a majority element is guaranteed to exist, Boyer-Moore Voting is an efficient solution with O(n) time and O(1) auxiliary space.
