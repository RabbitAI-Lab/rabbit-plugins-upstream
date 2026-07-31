## Description: <br>
Download OpenStreetMap features via Overpass API by bounding box, tag filter, or administrative place name, with GeoJSON, Shapefile, ZIP, and QA summary outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and data engineers use this skill to download public OpenStreetMap features for mapping, spatial analysis, QA checks, and downstream GIS workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security evidence says the package includes unrelated credential-handling code, local secret access, and hardcoded Earthdata credentials that users would not expect from an OpenStreetMap downloader. <br>
Mitigation: Treat installation as Review status until the publisher removes or splits out the credential module, revokes the hardcoded Earthdata credential, and discloses external services and local caches. <br>
Risk: The skill depends on unpinned Python package ranges for network and geospatial processing. <br>
Mitigation: Pin reviewed dependency versions before production deployment and run the skill in an isolated environment with only the required network access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/osm-data-download) <br>
- [OpenStreetMap](https://www.openstreetmap.org) <br>
- [Overpass API endpoint](https://overpass-api.de/api/interpreter) <br>
- [Nominatim search endpoint](https://nominatim.openstreetmap.org/search) <br>
- [Additional usage details](references/details.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Guidance] <br>
**Output Format:** [GeoJSON, ESRI Shapefile sidecars, zipped Shapefile bundles, JSON QA summaries, and Markdown command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call external Overpass and Nominatim services with requested coordinates or place names; OpenStreetMap data attribution and ODbL obligations remain the user's responsibility.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
