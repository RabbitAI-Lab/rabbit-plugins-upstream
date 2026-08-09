## Description: <br>
Download VIIRS nighttime light composite data from EOG/NOAA VNL and NASA LAADS sources, with annual and monthly products and optional regional bounding boxes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and geospatial analysts use this skill to search for and download VIIRS nightlights composites for urbanization, economic activity, population, and disaster-impact analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hardcoded Earthdata credentials and broad local credential-loading behavior may expose or reuse unintended account credentials. <br>
Mitigation: Remove and rotate the hardcoded credentials, avoid default credentials, and require explicit environment variables or reviewed secrets handling before installation in sensitive environments. <br>
Risk: Place-name resolution can send user-provided location text to external geocoding services. <br>
Mitigation: Use explicit bounding boxes for sensitive locations or review the geocoding behavior before enabling place-name lookup. <br>
Risk: Dependencies are not pinned to reviewed versions for deployment. <br>
Mitigation: Pin and review dependency versions before using the skill beyond local experimentation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-viirs-nightlights-download) <br>
- [EOG VNL products](https://eogdata.mines.edu/products/vnl/) <br>
- [EOG registration](https://eogdata.mines.edu/register/) <br>
- [README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with CLI commands, status text, URL listings, and downloaded data files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search and list modes can return available data or URLs; download mode writes VIIRS composite data to a user-selected output directory.] <br>

## Skill Version(s): <br>
5.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
