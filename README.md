# gemma_importer

This script creates an expression, gene, and column metadata file for a given GEMMA dataset and compresses it to be uploaded to NEMO easily.

Compressed data files from HTTP responses are also generated at the moment, this will be changed soon.

Certain libraries are used and should be installed.

# To run script in cmd line

```python3 gemma_importer.py [GEMMA dataset GEO name]```

# Files Created
```
expression.tab
genes.tab
observations.tab
metadata.xlsx
[dataset tag]_processed.tar.gz
```
