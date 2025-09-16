# Model Checking Results

This directory contains the results of model checking runs.

## File Naming Convention

- `small_model_<date>_<time>.json` - Results from small model exhaustive checking
- `large_model_simulation_<date>_<time>.json` - Results from large model simulation

## Interpreting Results

The JSON output from TLC contains:

- `states`: Number of distinct states explored
- `diameter`: Length of the longest behavior found
- `invariants`: List of invariants and whether they were violated
- `properties`: List of temporal properties and whether they were violated

## Example Result

An example result for the small model might look like:

```json
{
  "states": 12456,
  "diameter": 15,
  "invariants": {
    "NoConflictingFinalization": true,
    "ChainConsistency": true,
    "CertificateUniqueness": true
  },
  "properties": {
    "Progress": true,
    "FastPathProgress": true,
    "BoundedFinalizationTime": true
  }
}