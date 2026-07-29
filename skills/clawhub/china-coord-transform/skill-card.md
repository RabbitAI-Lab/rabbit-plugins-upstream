## Description: <br>
Converts coordinates among WGS-84, GCJ-02, and BD-09 and supports control-point affine, Helmert, CSV, GeoJSON, and Shapefile workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT No Attribution License (MIT-0) <br>


## Use Case: <br>
Developers and GIS/data engineers use this skill to convert Chinese map coordinates and batch-process CSV, GeoJSON, or Shapefile data for visualization or approximate location workflows. It should not be used for surveying, legal, emergency, or other high-accuracy location decisions without validated local control points. <br>

### Deployment Geography for Use: <br>
Global, with China-specific coordinate conversions and accuracy caveats. <br>

## Known Risks and Mitigations: <br>
Risk: The server security review reports unrelated credential, geocoding, caching, and download code in the published artifact. <br>
Mitigation: Review the package before installation and avoid running it in environments with valuable API keys, .netrc entries, or sensitive location queries unless those components are removed or clearly scoped. <br>
Risk: The security guidance reports hardcoded Earthdata credential fallback behavior and helpers that can read local credentials. <br>
Mitigation: Install only in an isolated environment, remove hardcoded credential defaults, and prefer explicit short-lived environment variables or secrets managed outside the skill. <br>
Risk: Artifact documentation states the default GCJ-02 conversion is an approximate reverse-engineered method with systematic error and legal or factual reliability limits. <br>
Mitigation: Use the default method only for approximate visualization, and use locally validated control points or Helmert parameters for workflows that require higher accuracy. <br>
Risk: Artifact helper behavior includes network geocoding, location lookup caching, and file downloads. <br>
Mitigation: Run with network access disabled unless needed, review cache and output paths, and inspect requested URLs before allowing downloads. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/china-coord-transform) <br>
- [README](README.md) <br>
- [qgis-geohey-toolbox](https://github.com/GeoHey-Team/qgis-geohey-toolbox) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with Python and shell command snippets; may reference coordinate values, CSV, JSON, GeoJSON, or Shapefile outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Coordinate results depend on the selected transformation method and the quality of any user-provided control points.] <br>

## Skill Version(s): <br>
1.1.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
