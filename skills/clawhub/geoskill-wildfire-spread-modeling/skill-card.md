## Description:

Models wildfire spread with a cellular automaton that accounts for fuel, moisture, slope, wind speed, and wind direction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers and geospatial analysts use this skill to run local wildfire spread simulations from synthetic data or local multi-band GeoTIFF inputs and inspect burned-area, arrival-time, and parameter outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security review reports unrelated vendored downloader, geocoder, and credential-handling code with hardcoded credentials.

Mitigation: Review or remove credentials.py, safe_download.py, and network geocoding before installation; rotate embedded Earthdata credentials if they are real.

Risk: The server security guidance warns against use in sensitive environments unless network geocoding and local credential access are controlled.

Mitigation: Disable or clearly control third-party geocoding and local credential access, and prefer synthetic or local-input operation when network access is not required.

Risk: The server security guidance calls out dependency pinning as a deployment concern.

Mitigation: Pin and review numpy, rasterio, and scipy before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-wildfire-spread-modeling)
- [README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Files, JSON, Text]

**Output Format:** [GeoTIFF rasters, JSON parameter and manifest files, and concise CLI text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include burned_area.tif, arrival_time.tif, fire_params.json, and output-manifest.json.]

## Skill Version(s):

1.0.0 (source: server release metadata; script VERSION agrees)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
