# DEV.md — phenology-metrics

## Goal
Extract phenological metrics from NDVI/EVI time series data.

## Data Source
Local processing of NDVI/EVI time series (CSV or multi-band GeoTIFF stack).

## Core Functions
1. **extract** — Extract phenology metrics from time series
2. **fit** — Fit double logistic curve to time series
3. **plot-data** — Generate fitted curve data for plotting

## Key Metrics
- SOS (Start of Season)
- EOS (End of Season)
- LOS (Length of Season)
- Peak value
- Peak date
- Amplitude
- Integral (season area)

## Methods
- Threshold (10%/50% of amplitude)
- Derivative (inflection points)
- Logistic fitting (double logistic)

## Dependencies
- numpy, scipy (curve fitting), pandas

## Verification
1. `python scripts/phenology-metrics.py --help` works
2. Subcommand help works
