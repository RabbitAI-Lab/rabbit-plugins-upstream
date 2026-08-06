## Description: <br>
Generates slope, aspect, hillshade, contour, curvature, flow direction, and accumulation terrain products from DEM data using pure Python. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and geospatial engineers use this skill to guide terrain derivative generation from DEM GeoTIFF files, including terrain visualization, hydrology preprocessing, and batch terrain-product workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The referenced Python terrain-analysis tool is not included in the inspected artifact, so commands shown by the skill may not run until the implementation file is supplied. <br>
Mitigation: Verify that dem-terrain-analysis.py is present and functional before relying on generated commands or batch workflows. <br>
Risk: Documentation for watershed and viewshed behavior may be incomplete or inconsistent. <br>
Mitigation: Review generated parameters and outputs for watershed and viewshed tasks before using results in operational decisions. <br>
Risk: Batch terrain processing can write multiple output files from local DEM inputs. <br>
Mitigation: Use only DEM files intended for processing and review output paths before running batch commands. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown with inline bash commands and file-output descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Describes GeoTIFF and GeoJSON terrain-analysis outputs such as slope, aspect, hillshade, contours, curvature, flow direction, and flow accumulation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
