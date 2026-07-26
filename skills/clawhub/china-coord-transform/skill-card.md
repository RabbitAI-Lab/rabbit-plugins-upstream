## Description: <br>
Converts coordinates among WGS-84, GCJ-02, and BD-09, with approximate GCJ-02 formulas, control-point affine or polynomial fitting, Helmert transforms, and batch GeoJSON or Shapefile conversion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT No Attribution License (MIT-0) <br>


## Use Case: <br>
Developers and GIS practitioners use this skill to convert individual points, CSV files, and vector geospatial files among China-related coordinate systems. It is appropriate for approximate visualization workflows by default, with higher-accuracy workflows requiring user-supplied control points and validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Approximate coordinate conversion can produce misleading locations when used for surveying, legal, emergency, or evidence-grade decisions. <br>
Mitigation: Use method 1 only for approximate visualization or product display, and use validated control points with method 2 or 3 for higher-accuracy workflows. <br>
Risk: Batch and vector workflows read and write user-specified local files. <br>
Mitigation: Run the skill only on intended input files and review generated CSV, JSON, GeoJSON, or Shapefile outputs before downstream use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/china-coord-transform) <br>
- [Homepage](https://github.com/ruiduobao/china-coord-transform) <br>
- [qgis-geohey-toolbox](https://github.com/GeoHey-Team/qgis-geohey-toolbox) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python and shell command examples; CLI output may be text, CSV, JSON parameters, GeoJSON, or Shapefile artifacts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python; Shapefile support requires optional pyshp.] <br>

## Skill Version(s): <br>
1.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
