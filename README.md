# Cache Eviction Policies

## Student
- Antonio Diaz, 73464639

## Repository Structure

- `src/` contains the source code
- `data/` contains example and test input/output files
- `tests/` reserved for any additional custom test cases

## Build / Compile Instructions

No compilation is required for this project because it is implemented in Python.

## How to Run

The repository includes:

- `data/example.in` as a sample input file
- `data/example.out` as the corresponding expected output file

The expected output can be reproduced by running:

```bash
python src/main.py data/example.in
```

You can also run the larger test files with:

```bash
python src/main.py data/file1.in
python src/main.py data/file2.in
python src/main.py data/file3.in
```

## Assumptions

- Input files follow the format:
  - first line: `k m`
  - second line: `r1 r2 ... rm`
- Requests are integer IDs
- The program checks that the number of requests matches `m`

## Question 1: Empirical Comparison

| Input File | k | m | FIFO | LRU | OPTFF |
|-----------|---|---|------|-----|-------|
| file1.in | 3 | 60 | 48 | 36 | 28 |
| file2.in | 4 | 64 | 54 | 51 | 32 |
| file3.in | 5 | 71 | 59 | 67 | 31 |

For all three input files, OPTFF had the fewest cache misses.

FIFO and LRU varied depending on the request pattern. In file1 and file2, LRU performed better than FIFO. In file3, FIFO performed better than LRU. This shows that while LRU often does well, it is not always better than FIFO on every sequence.

## Question 2: Bad Sequence for LRU or FIFO

For `k = 3`, the following request sequence shows that OPTFF can incur strictly fewer misses than both FIFO and LRU on this sequence:

```txt
3 12
1 2 3 4 1 2 5 1 2 3 4 5
```

The miss counts on this sequence were:

- FIFO: 9
- LRU: 10
- OPTFF: 7

This shows that such a sequence does exist. OPTFF performs better because it uses knowledge of future requests and evicts the item whose next use is farthest in the future. FIFO does not consider future use at all, and LRU only uses past accesses, so both can make worse eviction choices.

## Question 3: Prove OPTFF is Optimal

We prove that OPTFF (Belady’s Farthest-in-Future algorithm) is optimal using an exchange argument.

Let `A` be any offline algorithm that knows the entire request sequence in advance. Suppose that at some point, OPTFF and `A` have made the same decisions up to some eviction step, and now they make different eviction choices.

At this miss, both algorithms have the same cache contents just before eviction. Suppose OPTFF evicts item `x`, while `A` evicts a different item `y`.

By definition of OPTFF, item `x` is the item whose next request occurs farthest in the future (or never occurs again). Therefore, the next use of `x` is no earlier than the next use of `y`.

Now modify algorithm `A` so that at this step it evicts `x` instead of `y`, and afterward behaves exactly like `A` except for this change. Between this eviction step and the next request to either `x` or `y`, the modified algorithm cannot do worse than `A`, because `x` is needed no sooner than `y`. If `y` is requested before `x`, then keeping `y` in the cache is at least as good as keeping `x`. If `x` is never requested again, then evicting `x` is clearly safe.

So we can replace `A`’s choice with OPTFF’s choice without increasing the number of misses. Repeating this argument step by step, we can transform `A` into an algorithm that makes exactly the same choices as OPTFF, without increasing the number of cache misses.

Therefore, no offline algorithm can have fewer misses than OPTFF on any request sequence. Hence, OPTFF is optimal.