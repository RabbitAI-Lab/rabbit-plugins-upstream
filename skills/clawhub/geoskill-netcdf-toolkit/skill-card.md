## Description: <br>
Process NetCDF/HDF files by inspecting metadata, extracting variables, subsetting by time or bounding box, and converting variables to GeoTIFF. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to guide local NetCDF/HDF inspection, variable extraction, raster conversion, and spatial or temporal subsetting workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The from-place command may send place names, dates, bounding boxes, and dataset requests to external geocoding or data services despite local-only documentation. <br>
Mitigation: Use only info, convert, extract, and subset for local-only workflows; disable or avoid from-place unless the external services and adjacent downloader tools are approved. <br>
Risk: Geospatial processing dependencies and adjacent downloader tools can change behavior if installed without version control. <br>
Mitigation: Install in a locked environment with reviewed dependency versions before using the skill on sensitive or production data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-netcdf-toolkit) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, files] <br>
**Output Format:** [Markdown with inline shell commands; generated files may include GeoTIFF, NetCDF, GeoJSON, CSV, and JSON metadata outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The core commands read and write local files; the from-place command may invoke external geocoding or downloader tools.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
