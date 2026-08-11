## Description: <br>
Verifies agricultural subsidy compliance by overlaying high-resolution crop classification on declared parcels for difference detection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Agricultural program analysts, auditors, and developers use this skill to compare declared parcel crop fractions with NDVI-derived crop classification, flag suspected over- or under-declarations, and produce geospatial audit artifacts for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled credential, network, cache, and download helpers conflict with the documented offline-only privacy posture. <br>
Mitigation: Remove or disable those helpers before deployment, or document them clearly and require explicit user control before any credential access, cache writes, geocoding, or downloads. <br>
Risk: The package may read home-directory secrets or environment credentials in sensitive environments. <br>
Mitigation: Review the package before installation, run it in an isolated environment, and provide only the credentials needed for the intended local verification workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-agriculture-subsidy-verification) <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, GeoTIFF, GeoJSON, Text] <br>
**Output Format:** [GeoTIFF crop and parcel rasters, JSON verification report and manifest, GeoJSON flagged parcels, and console text summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are written to a local output directory; NoData pixels are excluded from parcel statistics.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and script VERSION; artifact CHANGELOG/openai.yaml list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
