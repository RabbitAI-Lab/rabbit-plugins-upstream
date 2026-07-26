## Description: <br>
Generates terrain derivatives such as slope, aspect, hillshade, contours, curvature, flow direction, and accumulation from DEM GeoTIFF data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and data engineers use this skill to run local command-line terrain analysis on DEM GeoTIFF files and generate derived GeoTIFF or GeoJSON outputs for mapping, hydrology, and visibility workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The tool reads local DEM files and writes terrain output files, so an incorrect output path or batch directory can overwrite or create unexpected files. <br>
Mitigation: Review input and output paths before running commands, especially batch mode on large datasets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/dem-terrain-analysis) <br>
- [README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with bash command examples; runtime outputs are GeoTIFF and GeoJSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes local DEM files; batch mode can create multiple terrain product files in an output directory.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
