## Description:

Smooths and reconstructs NDVI time series with Savitzky-Golay filtering or spline interpolation, producing regular time-series GeoTIFFs and smoothing parameters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers and geospatial analysts use this skill to smooth noisy NDVI time-series rasters, reconstruct regular vegetation-index products, and compare smoothing parameters for local or synthetic datasets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled helper modules can read local credential stores, use hardcoded Earthdata credentials, contact third-party geocoding services, or download arbitrary URLs if invoked.

Mitigation: Review or remove the bundled credential, downloader, and geocoding helpers before installation, and use the core smoothing command only after that review is complete.

Risk: The main smoothing workflow is local, but optional place resolution can contact external geocoding services.

Mitigation: Use explicit bounding boxes or synthetic mode when network access is not intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-temporal-interpolation)
- [Publisher profile](https://clawhub.ai/user/ruiduobao)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands]

**Output Format:** [GeoTIFF raster files, JSON smoothing parameters, JSON run manifest, and console status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are written locally to the selected output directory.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
