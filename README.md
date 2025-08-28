# Bitmap Indexing with WAH Compression

This project implements a **bitmap indexing system** in Python, with support for **Word-Aligned Hybrid (WAH) compression**.  
It demonstrates how categorical data can be converted into binary vectors and then compressed for efficient storage and querying — a common technique in **databases** and **information retrieval systems**.

---

## Overview

1. **Bitmap Index Creation**
   - Input file format:  
     ```
     animal,age,adopted
     ```
     Example:
     ```
     dog,5,True
     cat,22,False
     ```
   - Encoded into fixed-length bitmaps:
     - **Breed** (`bird`, `cat`, `dog`, `turtle`) → 4-bit code  
     - **Age range** (1–100, in 10-year bins) → 10-bit code  
     - **Adopted flag** (`True`/`False`) → 2-bit code  
   - Each record becomes a binary vector:  
     ```
     breed_bits + age_bits + adopted_bits
     ```

2. **Compression with WAH**
   - Splits the bitmap index into **columns**.  
   - Applies **Word-Aligned Hybrid (WAH) compression** to each column.  
   - Supports word sizes of **8, 16, 32, or 64 bits**.  
   - Produces compact, run-length encoded bitmaps that save space while enabling fast bitwise operations.

---

## Usage

### Generate a Bitmap Index
```python
create_index('animals.txt', 'write_up/', sorted=False)
