## Description: <br>
Computes Canadian Forest Fire Weather Index components from daily meteorological data and writes fire danger class rasters plus a spatial-mean time series. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
GIS, wildfire, climate, and emergency-planning teams use this skill to evaluate fire weather conditions for a bounding box or local meteorological raster. It supports local four-band GeoTIFF input and offline synthetic data generation for repeatable analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release security evidence reports under-disclosed network, cache, and credential helper code outside the documented local FWI command. <br>
Mitigation: Review the package before use in sensitive environments and remove or clearly disclose unused geocoding, downloader, cache, and credential helpers before deployment. <br>
Risk: The release security guidance identifies hardcoded Earthdata credentials in the package. <br>
Mitigation: Delete the hardcoded credentials, rotate any affected credentials, and verify no secrets remain before installation or redistribution. <br>
Risk: The release security guidance notes unpinned dependencies. <br>
Mitigation: Pin and review dependencies before deployment, especially in regulated or sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-fire-weather-index) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, GeoTIFF rasters, JSON, Text] <br>
**Output Format:** [GeoTIFF component and danger-class rasters, JSON time series, JSON run manifest, and console status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces final-day FFMC, DMC, DC, ISI, BUI, and FWI raster outputs plus daily spatial means.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence and script VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
