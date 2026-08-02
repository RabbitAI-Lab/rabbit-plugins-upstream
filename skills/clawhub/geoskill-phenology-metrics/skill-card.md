## Description: <br>
Extracts SOS, EOS, LOS, peak value/date, amplitude, and integral phenology metrics from NDVI/EVI time series using threshold, derivative, or logistic methods. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and geospatial practitioners use this skill to compute vegetation phenology metrics from local NDVI/EVI CSV or GeoTIFF time series and generate CSV or JSON result files for downstream analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security evidence reports bundled hardcoded Earthdata credentials. <br>
Mitigation: Do not install or use the package until the credentials are removed and rotated; require users to provide their own credentials through environment variables or an approved credential store. <br>
Risk: Security evidence reports under-disclosed network and place-resolution behavior despite local-only privacy statements. <br>
Mitigation: Avoid the from-place workflow for sensitive locations unless third-party geocoding and download traffic are acceptable; use local CSV or GeoTIFF inputs when local-only processing is required. <br>
Risk: Phenology metrics can be misleading when input time series are noisy, sparse, or weakly seasonal. <br>
Mitigation: Review QA output and fit quality, compare threshold, derivative, and logistic methods, and validate results before operational or commercial use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-phenology-metrics) <br>
- [README](README.md) <br>
- [Skill definition](SKILL.md) <br>
- [Development notes](DEV.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands; generated phenology results are CSV or JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can generate fitted-curve CSV files and QA JSON summaries when requested.] <br>

## Skill Version(s): <br>
5.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
