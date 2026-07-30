## Description: <br>
Downloads VIIRS nighttime light annual and monthly composites from EOG/NOAA VNL and NASA LAADS, with optional regional bounding-box subsetting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT No Attribution (MIT-0) <br>


## Use Case: <br>
External developers, geospatial analysts, and researchers use this skill to search for or download VIIRS annual and monthly nightlight composites for regional analysis using a year, product, bounding box, place, or preset. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes an unrelated credential helper with a real-looking hardcoded NASA Earthdata password and broad local-secret handling. <br>
Mitigation: Remove the embedded password, rotate affected credentials, and review the credential helper before installing or deploying the skill. <br>
Risk: The skill can use online geocoding and local AOI caching for free-form place resolution. <br>
Mitigation: Clearly disclose the geocoding and cache behavior; for sensitive locations, prefer explicit --bbox values or known presets. <br>
Risk: Dependencies are not pinned. <br>
Mitigation: Pin and review dependencies before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/viirs-nightlights-download) <br>
- [EOG VIIRS Nighttime Lights products](https://eogdata.mines.edu/products/vnl/) <br>
- [EOG account registration](https://eogdata.mines.edu/register/) <br>
- [NASA Worldview snapshot API](https://worldview.earthdata.nasa.gov/api/v1/snapshot) <br>
- [NASA LAADS DAAC](https://ladsweb.modaps.eosdis.nasa.gov) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, files, shell commands, guidance] <br>
**Output Format:** [CLI text output, JSON search results or URL lists, optional QA JSON summaries, and downloaded GeoTIFF .tif.gz files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Downloads may require a free EOG account; --list-urls can produce URLs for manual authenticated retrieval.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
