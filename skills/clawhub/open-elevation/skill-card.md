## Description: <br>
Batch query elevation data from the Open-Elevation public API for single-point and multi-point latitude/longitude coordinates, with CSV or JSON output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and data teams use this skill to retrieve elevation values for coordinates or CSV batches and incorporate the results into analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Coordinates sent to public third-party services may reveal sensitive locations. <br>
Mitigation: Avoid sensitive or private locations unless the user accepts external sharing, and use an internal elevation source when location confidentiality is required. <br>
Risk: The security summary reports unrelated credential-handling code with a hardcoded Earthdata password. <br>
Mitigation: Remove unrelated credential helpers, remove and rotate embedded credentials, and rescan before deployment. <br>
Risk: The security guidance calls out unpinned or loosely bounded dependencies. <br>
Mitigation: Pin approved dependency versions and install the skill in an isolated environment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/open-elevation) <br>
- [Open-Elevation](https://open-elevation.com/) <br>
- [Open-Elevation Lookup API](https://api.open-elevation.com/api/v1/lookup) <br>
- [SRTM Global Data](https://www2.jpl.nasa.gov/srtm/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, code, files, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands; generated data as CSV or JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Batch requests should respect the public API limit of up to 100 points per request.] <br>

## Skill Version(s): <br>
0.3.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
