## Description:

Classifies wetland types and computes area statistics with rule-based thresholds that fuse NDWI/MNDWI, NDVI, topographic depression, and SAR backscatter inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers, GIS analysts, and remote-sensing teams use this skill to run local wetland classification workflows over a bounding box or a local four-band raster. It produces class rasters, area statistics, and run manifests for baseline surveys and preliminary coastal, lakeshore, mangrove, or swamp inventories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The advertised wetland mapper mostly runs offline, but the package includes undocumented network, caching, and credential-helper code.

Mitigation: Review or remove unused geoskill core helper modules, especially credentials.py and aoi.py, before installation or deployment.

Risk: If the helper modules are used, place names may be sent to third-party geocoders and cached locally, and credentials may be exposed unintentionally.

Mitigation: Treat place names as potentially disclosed to third-party services, review local cache behavior, and verify credential handling before shared or production use.

Risk: Unpinned dependencies can change behavior across environments.

Mitigation: Pin numpy, rasterio, and scipy versions before shared or production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-wetland-mapping)
- [README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)
- [Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Files, JSON, Guidance]

**Output Format:** [Markdown guidance with CLI commands; local workflow outputs include GeoTIFF and JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primary generated files are wetland_class.tif, area_stats.json, and output-manifest.json.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
