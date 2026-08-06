## Description:

Performs bicubic 2x/4x geospatial image super-resolution and produces a super-resolved GeoTIFF plus PSNR quality metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers and geospatial analysts use this skill to upscale low-resolution GeoTIFF imagery or generate synthetic test imagery for local 2x/4x super-resolution experiments with PSNR-based quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security scan reports a suspicious artifact surface: the package presents as an offline super-resolution tool but includes undisclosed network geocoding, downloading, credential-loading code, and hardcoded Earthdata credentials.

Mitigation: Review the package before installing or executing; remove or clearly separate the network and credential modules and any hardcoded credentials before deployment.

Risk: The server security guidance notes code that can read local secret files.

Mitigation: Run the skill in a least-privilege environment and inspect filesystem access before using it on systems with sensitive home-directory credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-super-resolution)
- [README](README.md)
- [Skill instructions](SKILL.md)

## Skill Output:

**Output Type(s):** [Files, JSON, Analysis]

**Output Format:** [GeoTIFF raster file, JSON QA metrics, JSON output manifest, and optional console text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces super_resolved.tif, qa.json, and output-manifest.json in the selected output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata and CLI version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
