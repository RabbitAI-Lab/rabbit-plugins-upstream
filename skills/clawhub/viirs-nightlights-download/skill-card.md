## Description: <br>
Download VIIRS nighttime light composite data from public sources, including EOG/NOAA VNL and NASA LAADS, with annual and monthly composites and regional bounding-box subsetting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, geospatial analysts, and researchers use this skill to search for and download VIIRS nighttime-light composites for regional analysis, urbanization studies, population estimation, and disaster-impact assessment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Place-name lookup may contact third-party geocoding services. <br>
Mitigation: Use explicit --bbox values or offline presets for sensitive locations. <br>
Risk: Dependency hygiene requires review before installation. <br>
Mitigation: Pin or upgrade dependencies according to the deployment environment before use. <br>


## Reference(s): <br>
- [EOG VIIRS Nighttime Lights Products](https://eogdata.mines.edu/products/vnl/) <br>
- [NASA LAADS DAAC](https://ladsweb.modaps.eosdis.nasa.gov) <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/viirs-nightlights-download) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands; downloaded raster files and optional JSON QA sidecars when executed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports search, download, regional bbox/place selection, and optional run-summary output.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
