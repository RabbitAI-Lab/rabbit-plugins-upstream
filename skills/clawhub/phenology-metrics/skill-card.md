## Description: <br>
Extracts phenological metrics from NDVI/EVI time series data, including start and end of season, season length, peak value and date, amplitude, and integral. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and analysts use this skill to compute vegetation phenology metrics from local CSV time series or multi-band GeoTIFF stacks. It supports threshold, derivative, and double logistic workflows for exploratory and production geospatial analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes under-disclosed networked place lookup and satellite data download behavior despite local-only wording. <br>
Mitigation: Review the skill before installing and use it only when networked lookup and download behavior is acceptable for the deployment environment. <br>
Risk: The bundled credential defaults include a hardcoded Earthdata password. <br>
Mitigation: Remove or rotate the exposed Earthdata credential and configure personal credentials through environment variables or a secure local store. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/phenology-metrics) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Files] <br>
**Output Format:** [Markdown guidance with shell commands; generated outputs are CSV or JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce fitted-curve plot data and per-pixel phenology result files for batch workflows.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
