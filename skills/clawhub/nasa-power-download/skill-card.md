## Description: <br>
Downloads NASA POWER meteorological and solar energy data, including solar radiation, temperature, precipitation, wind, humidity, and other parameters, for point or regional queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, data analysts, and energy or environmental teams use this skill to fetch NASA POWER weather and solar resource datasets for a point location or bounded region and save the results for analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security summary flags under-disclosed credential-management code and a hardcoded Earthdata account fallback in bundled helper code. <br>
Mitigation: Review the credential helper before installation, remove or disable fallback credentials, avoid running with unnecessary secret-bearing environment variables, and install in an isolated environment. <br>
Risk: Place-name resolution can send user-provided place names to external geocoding services. <br>
Mitigation: Use exact latitude and longitude or an explicit bounding box when location query privacy matters. <br>
Risk: The server security guidance calls out dependency risks. <br>
Mitigation: Review and pin dependency versions before deployment, and run the skill in an environment isolated from sensitive files and credentials. <br>


## Reference(s): <br>
- [NASA POWER API](https://power.larc.nasa.gov/api/) <br>
- [NASA POWER Documentation](https://power.larc.nasa.gov/docs/) <br>
- [NASA POWER Project](https://power.larc.nasa.gov/) <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/nasa-power-download) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands; generated data files are CSV or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The downloader accepts NASA POWER parameter names, date ranges, point coordinates, bounding boxes, temporal resolution, and output format options.] <br>

## Skill Version(s): <br>
0.3.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
