## Description:

Compute street canyon height-to-width ratio and sky view factor (SVF) from a digital surface model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers, GIS analysts, and urban climate researchers use this skill to derive street canyon morphology metrics from local DSM GeoTIFF data or synthetic offline scenes for urban climate, thermal environment, and radiation analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release includes network, download, caching, and credential-handling modules that are not central to the documented local urban canyon workflow.

Mitigation: Review or remove those unused modules before installation, and run the skill only with the documented local DSM/DTM or synthetic offline paths unless the extra modules have been audited.

Risk: If invoked, bundled helper modules can contact third-party services or read local credential stores.

Mitigation: Execute in an environment with network access and secret stores disabled unless those behaviors are explicitly needed and reviewed.

## Reference(s):

- [Skill README](README.md)
- [Skill source instructions](SKILL.md)
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-urban-canyon-analysis)
- [ClawHub publisher profile](https://clawhub.ai/user/ruiduobao)

## Skill Output:

**Output Type(s):** [Files, Analysis, Shell commands, Guidance]

**Output Format:** [GeoTIFF, JSON, and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces urban_canyon.tif, canyon_stats.json, and output-manifest.json from local DSM/DTM inputs or synthetic offline data.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact openai.yaml and CHANGELOG report 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
