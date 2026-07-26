# forest-carbon-estimate - Development Doc

## Purpose
Estimate forest carbon stock from remote sensing data using multiple methods.

## Methods
1. **BEF (Biomass Expansion Factor)**: AGB × BEF = Total biomass
2. **Allometric equations**: AGB = f(height, diameter) — simplified from height or NDVI
3. **IPCC Tier 1/2**: Default biomass factors by forest type/eco-region

## Calculation Chain
- AGB (Above-ground biomass) from height or NDVI
- BGB (Below-ground biomass) = AGB × root-shoot ratio (default 0.26)
- Total biomass = AGB + BGB
- Carbon stock = Total biomass × carbon fraction (default 0.47)

## Uncertainty Analysis
- Monte Carlo: sample input parameters from distributions, propagate through calculation
- Report mean, std, 5th/95th percentiles

## CLI Design
```
forest-carbon-estimate estimate --input --method --output
forest-carbon-estimate uncertainty --input --method --iterations --output
forest-carbon-estimate report --input --output
```

## Dependencies
- numpy>=1.21.0
- rasterio>=1.3.0 (for GeoTIFF input)

## Implementation Notes
- Input: GeoTIFF (height/biomass band) or CSV with plot data
- Support --agb-band for multi-band GeoTIFF
- Default parameters from IPCC guidelines
- Output: carbon stock map (GeoTIFF) + summary statistics (JSON)
