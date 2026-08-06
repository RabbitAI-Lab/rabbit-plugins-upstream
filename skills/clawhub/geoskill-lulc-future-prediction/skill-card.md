## Description: <br>
Predicts target-year land cover using Markov transition probabilities and a simplified CA-Markov model, including urban expansion simulation and uncertainty. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and GIS analysts use this skill to run offline land-use and land-cover future projections from a WGS84 bounding box, synthetic scenario, or local two-band GeoTIFF. It produces projected land-cover rasters, uncertainty data, transition statistics, and a run manifest for downstream review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package bundles unrelated credential, downloader, and online geocoding code, including a hardcoded Earthdata password. <br>
Mitigation: Review or remove the unrelated vendored modules before installation, especially credentials.py, safe_download.py, _place.py, and _geoskill_core/aoi.py, and revoke or rotate the exposed Earthdata credential. <br>
Risk: Dependencies are not pinned or locked. <br>
Mitigation: Pin or lock dependencies before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-lulc-future-prediction) <br>
- [README](README.md) <br>
- [Skill definition](SKILL.md) <br>
- [Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Configuration] <br>
**Output Format:** [GeoTIFF and JSON files with optional console text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary outputs include predicted_lulc.tif, uncertainty.tif, transition_probabilities.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
