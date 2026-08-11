## Description: <br>
Multi-temporal SAR backscatter analysis computes per-pixel mean, standard deviation, amplitude, coefficient of variation, and polarization ratio from sigma-zero time-series data, producing a multi-band statistics GeoTIFF and time-series JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to summarize local or synthetic multi-temporal SAR backscatter cubes for change detection, phenology monitoring, and time-series analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes under-disclosed helper modules for network access, downloads, and credential handling, including a hardcoded Earthdata password noted by the security evidence. <br>
Mitigation: Review and audit the bundled helper modules before installation, run the skill in an isolated environment, and avoid exposing sensitive .netrc files, local geoskill secrets, or API keys unless those modules are removed or trusted. <br>


## Reference(s): <br>
- [README.md](README.md) <br>
- [ClawHub skill release](https://clawhub.ai/ruiduobao/skills/geoskill-sar-backscatter-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Analysis] <br>
**Output Format:** [GeoTIFF files, JSON manifests, JSON time-series files, and optional console status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary outputs include backscatter_stats.tif, timeseries.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
