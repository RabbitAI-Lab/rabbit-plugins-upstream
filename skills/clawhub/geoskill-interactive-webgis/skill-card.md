## Description: <br>
Configure a lightweight WebGIS with query support as a self-contained HTML app. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to generate a self-contained interactive WebGIS app from local GeoTIFF or vector inputs, or from synthetic data for testing. The generated app supports layer toggles, point queries, raster elevation lookup, attribute filtering, and point density outputs without a backend. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence says the package includes credential, network, download, and persistent-cache helpers that are under-disclosed for a skill advertised as self-contained and offline. <br>
Mitigation: Review the package before installation and confirm whether those helpers are needed; remove or clearly disclose credential helpers, hardcoded Earthdata credentials, remote geocoding, home-directory cache behavior, and browser-time external map or CDN access before deployment. <br>
Risk: The main WebGIS workflow appears scoped to local inputs and outputs, but browser-time external map or CDN access may still occur. <br>
Mitigation: Use synthetic or local inputs for offline runs and verify generated HTML dependencies before sharing or deploying the app in restricted environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-interactive-webgis) <br>
- [README](README.md) <br>
- [LICENSE](LICENSE) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated artifact files include HTML, JSON, GeoJSON, GeoTIFF, and manifest JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The primary generated file is webgis.html, with webgis_data.json, features.geojson, density.tif, and output-manifest.json produced during normal runs.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
