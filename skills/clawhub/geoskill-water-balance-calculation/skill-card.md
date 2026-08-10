## Description:

Per-pixel water balance computation for P = ET + Q + delta S with closure residual assessment, producing component and residual GeoTIFFs plus a JSON report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers and hydrology or GIS analysts use this skill to compute per-pixel water balance over a WGS84 bounding box or local precipitation raster, validate synthetic workflows offline, and assess closure residuals before hydrologic data analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled support modules include network, geocoding, and credential-handling code with a hardcoded password.

Mitigation: Review or remove _geoskill_core/credentials.py, _geoskill_core/aoi.py, _place.py, and safe_download.py before installing, and treat the exposed Earthdata fallback credential as compromised.

Risk: The offline behavior claim may only apply when execution is limited to the main water-balance script.

Mitigation: Restrict execution to geoskill-water-balance-calculation.py when offline-only operation is required, and scan any bundled helper modules before deployment.

## Reference(s):

- [README.md](README.md)
- [SKILL.md](SKILL.md)
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-water-balance-calculation)

## Skill Output:

**Output Type(s):** [Shell commands, Files, Analysis]

**Output Format:** [Markdown guidance for running the CLI; the CLI writes GeoTIFF, JSON, and manifest files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include balance_components.tif, closure_residual.tif, water_balance_report.json, and output-manifest.json.]

## Skill Version(s):

1.0.0 (source: release metadata; artifact openai.yaml and CHANGELOG list 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
