
# BAM Cell Barcode Extractor

This Python script extracts reads from a BAM file based on specified cell barcodes and creates separate BAM files for each barcode.

## Prerequisites

- Python 3.x
- pysam library

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required library:

   ```
   pip install pysam
   ```

## Usage

Run the script from the command line with the following syntax:

```
python bam_barcode_extractor.py <input_bam> <barcode_file> <output_directory>
```

### Parameters:

- `<input_bam>`: Path to the input BAM file
- `<barcode_file>`: Path to a text file containing cell barcodes (one per line)
- `<output_directory>`: Path to the directory where output BAM files will be saved

## Input Files

1. **BAM File**: A sorted and indexed BAM file containing aligned reads with cell barcode information in the CB tag.

2. **Barcode File**: A text file with one cell barcode per line. For example:
   ```
   AAACCTGAGAAACCAT
   AAACCTGAGAAACCGC
   AAACCTGAGAAACCCA
   ```

## Output

The script will create a separate BAM file for each cell barcode in the specified output directory. Each BAM file will be named after its corresponding cell barcode (e.g., `AAACCTGAGAAACCAT.bam`).

## How It Works

1. The script reads the input BAM file and the barcode file.
2. It creates a new BAM file for each unique barcode in the barcode file.
3. It then iterates through all reads in the input BAM file.
4. For each read, it checks the CB tag (cell barcode).
5. If the CB tag matches one of the barcodes from the barcode file, the read is written to the corresponding output BAM file.

## Notes

- Ensure that your BAM file has the CB tag for cell barcodes.
- The script assumes that the BAM file is sorted and indexed.
- Large BAM files may require significant processing time and memory.
