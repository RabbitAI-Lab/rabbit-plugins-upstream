## Description: <br>
Download global administrative boundary vector data (Shapefile / GeoJSON / GeoPackage / TopoJSON) for any country or multi-country region. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and mapping workflows use this skill to find countries by name or ISO code, inspect available administrative levels, and download boundary datasets as Shapefile, GeoJSON, GeoPackage, or TopoJSON files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The submitted package is incomplete and has dependency ambiguity around the local core modules and bare core dependency. <br>
Mitigation: Review the package before installation; include the intended local core modules or remove and justify the bare core dependency. <br>
Risk: Automatic fallback can move from geoBoundaries to GADM, whose usage terms differ from the default data source. <br>
Mitigation: Make fallback and license notices explicit to users, especially when downloaded data may be used commercially. <br>
Risk: Dependencies are version-ranged rather than pinned to known-safe versions. <br>
Mitigation: Pin dependencies to reviewed versions before deployment in controlled environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/world-boundary-download) <br>
- [geoBoundaries](https://www.geoboundaries.org/) <br>
- [GADM](https://gadm.org) <br>
- [Natural Earth CDN](https://naciscdn.org/naturalearth/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Files, Guidance] <br>
**Output Format:** [CLI output as JSON or plain text, plus downloaded geospatial files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Shapefile zip, GeoJSON, GeoPackage, or TopoJSON files and can write optional JSON run-summary sidecars.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
