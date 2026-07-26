## Description: <br>
Convert NetCDF/HDF files to GeoTIFF, extract variables, subset by time and spatial bbox, and inspect file metadata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial data engineers use this skill to inspect local NetCDF/HDF datasets, convert variables into GIS-ready outputs, and extract spatial or temporal subsets for downstream analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is marked suspicious because local-only claims are inconsistent with under-disclosed geocoding and remote-fetch behavior. <br>
Mitigation: For local-only deployments, use info, convert, extract, and subset workflows on local files; disable or restrict from-place, geocoding, and adjacent downloader paths. <br>
Risk: External place queries and downloader paths may send place queries to external services or fetch remote datasets. <br>
Mitigation: Document network behavior, require explicit operator approval for network-enabled commands, and pin dependencies before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/netcdf-toolkit) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, code, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands; CLI output may include text or JSON metadata and generated GeoTIFF, NetCDF, GeoJSON, or CSV files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local info, convert, extract, and subset workflows; from-place workflows may use external geocoding and adjacent downloader scripts.] <br>

## Skill Version(s): <br>
0.3.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
