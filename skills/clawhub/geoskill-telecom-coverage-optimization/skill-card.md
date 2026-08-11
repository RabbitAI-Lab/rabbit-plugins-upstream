## Description:

Simplified Okumura-Hata propagation with terrain and buildings to map coverage and blind spots for telecom planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers, telecom engineers, and network planners use this skill to estimate base-station signal strength, coverage masks, blind spots, and gap-filling recommendations from terrain, building, tower, and synthetic scene inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes credential and network helper code broader than the advertised offline telecom coverage workflow.

Mitigation: Review before installing in environments with valuable credentials; remove hardcoded Earthdata credential defaults and disable or clearly document local secret discovery and geocoding helpers.

Risk: Offline behavior may be misunderstood because synthetic mode is offline, while bundled helpers can perform geocoding and download operations.

Mitigation: Prefer synthetic or local-input runs when offline execution is required, and restrict network access unless geocoding or downloads are intentionally enabled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-telecom-coverage-optimization)
- [Publisher profile](https://clawhub.ai/user/ruiduobao)
- [README](artifact/README.md)
- [Skill instructions](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Files, JSON, GeoJSON, Geospatial raster, Analysis]

**Output Format:** [GeoTIFF signal and mask files, GeoJSON tower data, JSON coverage reports, and JSON run manifests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include signal_strength.tif, coverage_mask.tif, towers.geojson, coverage_report.json, and output-manifest.json.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
