## Description: <br>
Searches and downloads Terra and Aqua MODIS Land Surface Temperature products from NASA LAADS DAAC with GeoTIFF output and Earthdata authentication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and Earth observation workflows use this skill to search, list, and download MODIS LST granules for a date range and area of interest, then produce georeferenced raster outputs for analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Embedded Earthdata fallback credentials may be used silently. <br>
Mitigation: Remove or disable fallback credentials before installation and require users to provide their own Earthdata credentials or token explicitly. <br>
Risk: A real exposed Earthdata account may need remediation. <br>
Mitigation: Rotate any exposed account credentials and prefer a dedicated low-privilege NASA Earthdata account or token for this workflow. <br>
Risk: Place-name resolution can send sensitive place queries to external geocoding services. <br>
Mitigation: Use explicit bounding boxes for sensitive locations or confirm that external geocoding is acceptable before using place-name inputs. <br>
Risk: Local credential sources such as .netrc or config files may be used. <br>
Mitigation: Review local credential files and environment variables so the skill uses only intended credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-modis-lst-download) <br>
- [NASA LAADS DAAC](https://ladsweb.modaps.eosdis.nasa.gov/) <br>
- [NASA Earthdata Login](https://urs.earthdata.nasa.gov/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell commands and CLI parameter guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide searches, credential setup, URL listing, downloads, GeoTIFF outputs, and quality-control band interpretation.] <br>

## Skill Version(s): <br>
5.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
