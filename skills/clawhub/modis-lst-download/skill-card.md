## Description: <br>
Searches and downloads MODIS Land Surface Temperature (LST) products from NASA LAADS DAAC for Terra and Aqua products and outputs GeoTIFF files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and geospatial practitioners use this skill to find MODIS land-surface-temperature data by product, date range, and area of interest, then download or list matching NASA LAADS DAAC files for analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Earthdata credentials may be stored locally or used during network authentication. <br>
Mitigation: Prefer environment variables over the configure command, protect any local credential file, and rotate credentials if they may have been exposed. <br>
Risk: Place-name lookup can disclose sensitive locations to third-party geocoding services. <br>
Mitigation: Use explicit --bbox values and avoid --place for sensitive areas or private workflows. <br>
Risk: The release was flagged for review because credential handling and place lookup are broader than the documentation clearly discloses. <br>
Mitigation: Review the skill and pin or audit dependencies before using it in a controlled environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/modis-lst-download) <br>
- [NASA LAADS DAAC](https://ladsweb.modaps.eosdis.nasa.gov/) <br>
- [NASA Earthdata Login](https://urs.earthdata.nasa.gov/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with command examples; the included scripts can produce GeoTIFF files, URL lists, and optional QA JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Downloads require NASA Earthdata credentials; unauthenticated runs can list URLs when available.] <br>

## Skill Version(s): <br>
0.3.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
