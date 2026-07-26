## Description: <br>
Convert between vector GIS formats using only the Python standard library. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and geospatial engineers use this skill to convert local vector GIS files among Shapefile, GeoJSON, KML, GPX, GeoPackage, and CSV formats, inspect file metadata, and apply basic filters such as CRS selection, precision, field selection, and bounding boxes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes geocoding, caching, and generic download helpers beyond the documented offline converter, and those helpers can contact third-party services. <br>
Mitigation: Use vector-convert.py directly for local conversions and avoid invoking _place.py or _geoskill_core geocoding/download helpers unless external network access is intended. <br>
Risk: Users expecting a strict offline, zero-dependency converter may deploy extra modules that do not match that expectation. <br>
Mitigation: Review the package contents before deployment and remove the helper modules if the operating requirement is strictly local, offline conversion only. <br>


## Reference(s): <br>
- [Artifact README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/vector-convert) <br>


## Skill Output: <br>
**Output Type(s):** [files, text, JSON] <br>
**Output Format:** [Converted GIS files, JSON info or QA summaries, and brief CLI status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local conversion, file-info output, field filtering, bounding-box clipping, coordinate precision control, and optional QA JSON.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
