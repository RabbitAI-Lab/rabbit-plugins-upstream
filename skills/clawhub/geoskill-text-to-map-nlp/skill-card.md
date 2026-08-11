## Description:

Parses natural-language map requests into layer parameters and renders local thematic map outputs as PNG, GeoTIFF, GeoJSON, and JSON manifest files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and GIS users can use this skill to turn a plain-language map request or local GeoTIFF into offline thematic map artifacts for review, audit, or downstream geospatial workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled helper modules include network geocoding and download capabilities that are not central to the documented offline renderer.

Mitigation: Review the bundled helper modules before installation and remove or disable network-capable paths unless they are explicitly needed.

Risk: Bundled credential helper behavior may discover local credentials or include a hardcoded Earthdata credential fallback.

Mitigation: Inspect credential handling before deployment and remove fallback credentials or require explicit user-provided credentials.

Risk: The skill is marketed as offline while server security evidence flags under-disclosed auxiliary capabilities.

Mitigation: Document any non-offline behavior clearly and run the skill in a constrained environment until the auxiliary capabilities are accepted or removed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-text-to-map-nlp)
- [README](artifact/README.md)
- [Skill instructions](artifact/SKILL.md)
- [Release changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, code, guidance]

**Output Format:** [CLI guidance and generated files including PNG, GeoTIFF, GeoJSON, JSON, and a run manifest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally by default and writes outputs to the configured output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata and script VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
