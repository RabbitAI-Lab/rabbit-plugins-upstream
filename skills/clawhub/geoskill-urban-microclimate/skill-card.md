## Description:

Analyze urban heat island intensity and ventilation index from land surface temperature, NDVI, impervious surface and building morphology.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers, GIS analysts, and urban planning teams use this skill to estimate local heat-island intensity and ventilation indicators from local four-band GeoTIFF inputs or synthetic offline scenes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports a suspicious package because the artifact includes under-disclosed network, download, and credential-handling helpers, including hardcoded Earthdata credentials.

Mitigation: Review before installation, remove and rotate the hardcoded credentials, and remove unused helpers or document and gate them behind explicit user configuration.

Risk: The advertised CLI is local, but bundled helper modules can contact external geocoding or download services and read user credential files.

Mitigation: Run in a constrained environment by default and allow network access or credential-file access only when the user explicitly enables those helper paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-urban-microclimate)
- [Artifact README](README.md)
- [Artifact SKILL.md](SKILL.md)

## Skill Output:

**Output Type(s):** [Shell commands, Files, Analysis, JSON, Configuration]

**Output Format:** [GeoTIFF raster, JSON statistics, JSON run manifest, and console text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primary outputs are microclimate.tif, microclimate_stats.json, and output-manifest.json; synthetic mode runs offline.]

## Skill Version(s):

1.0.0 (source: server release metadata and CLI VERSION; artifact openai.yaml and CHANGELOG list 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
