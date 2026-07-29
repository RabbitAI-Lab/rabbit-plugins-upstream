## Description: <br>
Convert NetCDF and HDF files to GeoTIFF, extract variables, subset by time and spatial bounding box, and inspect file metadata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, data engineers, and geospatial analysts use this skill to inspect local NetCDF/HDF datasets and generate derived raster, subset, or metadata outputs for analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Embedded Earthdata credentials may expose or misuse a shared account. <br>
Mitigation: Remove embedded credentials, rotate the exposed password, and require user-supplied credentials through environment variables, .netrc, or a user-owned secrets file. <br>
Risk: Under-disclosed geocoding and download behavior may initiate network requests that users do not expect. <br>
Mitigation: Document network behavior clearly and require explicit user consent or an offline mode before place lookup or data download paths run. <br>
Risk: Credential and cache handling may be unclear to users reviewing whether the skill is appropriate for their environment. <br>
Mitigation: Clarify credential precedence, cache locations, secret redaction, and cleanup guidance in user-facing documentation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/netcdf-toolkit) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Files, JSON] <br>
**Output Format:** [Markdown guidance with bash commands; generated local GeoTIFF, NetCDF, JSON, GeoJSON, or CSV outputs when commands are run] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are written to the local filesystem and depend on the selected CLI subcommand and installed geospatial Python libraries.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
