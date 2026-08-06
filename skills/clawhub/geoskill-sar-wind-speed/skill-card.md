## Description: <br>
Retrieves sea-surface wind speed at 10 m height from SAR backscatter using a simplified CMOD5/CMOD7 empirical geophysical model and vectorized bisection retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and geospatial engineers use this skill to generate SAR-derived sea-surface wind speed fields for wind monitoring, cyclone structure analysis, ocean dynamics studies, and offshore wind resource assessment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes geocoding, generic downloading, local location caching, and credential-handling modules beyond the advertised offline SAR wind workflow. <br>
Mitigation: Review and remove or gate those bundled modules before installing in environments with private credentials or sensitive locations unless those behaviors are explicitly required. <br>
Risk: The advertised SAR command can run locally, but optional bundled modules may introduce network and credential exposure paths. <br>
Mitigation: Run the SAR workflow in a constrained environment and provide only the credentials and network access needed for the intended execution path. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-sar-wind-speed) <br>
- [Skill documentation](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Guidance] <br>
**Output Format:** [GeoTIFF and JSON files with console status output and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces wind_speed.tif, retrieval_params.json, and output-manifest.json; synthetic runs include QA metrics.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and script VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
