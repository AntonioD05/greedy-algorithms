## Repository Structure

- `src/` contains the source code
- `data/` contains example and test input/output files
- `tests/` reserved for any additional tests

## How to Run

Run the program with:

```bash
python src/main.py data/example.in
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