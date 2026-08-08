---
name: landslide-susceptibility
description: >
  Integrate terrain, geology, rainfall, land cover, roads, and historical
  landslide data to produce interpretable susceptibility zoning with spatial
  cross-validation.
---

# Landslide Susceptibility Assessment

Integrates terrain, geology, rainfall, land cover, roads, and historical
landslide data to produce interpretable susceptibility zoning with spatial
cross-validation.

## Trigger

Use when the user wants to:
- Produce a landslide susceptibility map for a region
- Compare statistical/ML models for landslide prediction
- Evaluate factor contributions to landslide susceptibility
- Generate susceptibility zoning with uncertainty estimates
- Validate landslide models with spatial cross-validation

## CLI Usage

```bash
# Synthetic demo mode (no input files needed)
python scripts/landslide_susceptibility.py --output-dir ./ls-output

# With custom model
python scripts/landslide_susceptibility.py --model random_forest --output-dir ./ls-output

# With custom parameters
python scripts/landslide_susceptibility.py \
  --model logistic_regression \
  --negative-sampling buffer \
  --cv-block-size 20 \
  --n-folds 5 \
  --class-schema five_class \
  --output-dir ./ls-output

# With custom factor config
python scripts/landslide_susceptibility.py \
  --factor-config ./my-factor-config.json \
  --output-dir ./ls-output
```

## Data Download

This skill can auto-fetch a DEM (Copernicus GLO-30, 30 m) from the Microsoft
Planetary Computer when given a bounding box + date range. The DEM is saved to
`<output-dir>/downloaded/` and the `output-manifest.json` will record the
collection, bbox, and fetch timestamp. (The landslide inventory itself is
**not** auto-downloaded — supply it via `--landslide-inventory`.)

```bash
# Fetch a DEM for the Beijing area and run the synthetic pipeline
python scripts/landslide_susceptibility.py \
  --bbox 116,39,117,40 \
  --date-range 2024-01-01,2024-12-31 \
  --output-dir ./ls-output

# Or via an AOI polygon file
python scripts/landslide_susceptibility.py \
  --aoi-file ./aoi.geojson \
  --output-dir ./ls-output
```

The `PYTHONPATH` must include the parent of `_geoskill_data_fetcher/`
(usually the same directory the 50 skills live in). Set it once:

```bash
export PYTHONPATH="/path/to/行业Skill创意-20260727"
```

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `--landslide-inventory` | None | Path to landslide inventory (GeoJSON/Shapefile) |
| `--factor-config` | None | Path to factor configuration JSON (default: references/factor_config.json) |
| `--model` | logistic_regression | Model type: logistic_regression, random_forest, slope_baseline |
| `--negative-sampling` | buffer | Negative sampling strategy: random, buffer, spatial_block |
| `--cv-block-size` | 20 | Spatial CV block size in pixels |
| `--n-folds` | 5 | Number of CV folds |
| `--class-schema` | five_class | Classification schema: five_class, four_class |
| `--output-dir` | ./ls-output | Output directory |

## Output

| File | Description |
|---|---|
| `susceptibility.tif` | Susceptibility probability map (0-1) |
| `susceptibility_zones.geojson` | Susceptibility zone polygons |
| `model_metrics.json` | Comprehensive model metrics with spatial CV results |
| `factor_importance.csv` | Factor importance rankings |
| `model_card.json` | Model card with limitations and metadata |
| `request.json` | Analysis request metadata |
| `dataset-manifest.json` | Dataset inventory |
| `output-manifest.json` | Output file inventory |
| `qa.json` | Quality assurance checks |

## Key Algorithms

### Spatial Block Cross-Validation
Divides the AOI into spatial blocks. Each fold uses distinct geographic
blocks for validation, preventing spatial autocorrelation from inflating
accuracy metrics. Block size should match the spatial autocorrelation range.

### Collinearity Check (VIF)
Computes Variance Inflation Factor for each factor. Factors with VIF > 5
are flagged as potentially collinear. High correlation pairs (|r| > 0.8)
are reported.

### Negative Sampling
Three strategies available:
- **random**: Uniform random sampling across AOI
- **buffer**: Samples drawn outside buffer zones around known landslides
- **spatial_block**: Stratified sampling across spatial blocks

### Model Types
- **logistic_regression**: Interpretable linear model with probability output
- **random_forest**: Ensemble of decision trees with permutation importance
- **slope_baseline**: Simple slope-threshold baseline for comparison

### Susceptibility Classification
Five-class: Very low (<0.2), Low (0.2-0.4), Moderate (0.4-0.6), High (0.6-0.8), Very high (>0.8)

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 2 | Argument error |
| 3 | Dependency missing |
| 6 | Data validation failure |
| 7 | Processing failure |

## Important Limitations

- Output is **susceptibility** (relative likelihood), NOT temporal probability or risk
- Requires trigger probability and exposure data for risk assessment
- Model accuracy depends on landslide inventory completeness
- Spatial transferability not guaranteed
- Not for engineering safety decisions without expert review

## References

- Fell, R., et al. (2008). Guidelines for landslide susceptibility, hazard and risk zoning for land-use planning.
- Reichenbach, P., et al. (2018). A review of statistically-based landslide susceptibility models.
- Budimir, M.E.A., et al. (2015). A systematic review of landslide probability zonation.
