## Description: <br>
Converts supported Ovital/Ovi Map .ovobj point labels and .ovkml point exports into validated WGS84 EPSG:4326 ESRI Shapefiles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and fieldwork teams use this skill to convert supported Ovital/Ovi Map point exports while preserving Chinese label names, source coordinates, WGS84 coordinates, point counts, and generated Shapefile sidecars. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The converter reads local input paths and can scan directories or replace existing output files when broad options are used. <br>
Mitigation: Use explicit input paths by default, review the output directory, and enable --recursive or --overwrite only when broader processing or replacement is intended. <br>
Risk: Incorrect coordinate assumptions can shift converted field locations. <br>
Mitigation: Leave --source-crs set to auto when possible, rely on OVKML OvCoordType values, and compare against a known point before forcing a coordinate-system override. <br>
Risk: Unsupported OVOBJ layouts, mixed OVKML coordinate types, tracks, polygons, attachments, encrypted files, or ODB databases are outside the supported conversion scope. <br>
Mitigation: Use the skill only for supported point-label inputs and treat clear parser errors as a signal to inspect or export the data in a supported format before conversion. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, generated ESRI Shapefile sidecars, and a JSON conversion report.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes .shp, .shx, .dbf, .prj, .cpg, and *_conversion_report.json files; output geometries are WGS84 EPSG:4326 point features.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
