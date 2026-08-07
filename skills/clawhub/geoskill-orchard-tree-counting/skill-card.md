## Description:

Counts orchard trees and estimates crown widths from canopy height models using peak detection and template matching.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers and geospatial analysts use this skill to run local orchard tree-counting workflows on CHM GeoTIFF inputs or synthetic scenes and review GeoTIFF, JSON, and console outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the package includes under-disclosed network, credential-reading, cache, and hardcoded credential code outside the stated offline orchard-counting purpose.

Mitigation: Review the package before installing, remove or isolate unused credential/download/geocoding modules, and rotate any real credentials before release or deployment.

Risk: The security guidance notes possible network geocoding and home-directory cache behavior.

Mitigation: Run the local CHM or synthetic workflow in a restricted environment with outbound network and home-directory writes limited unless those behaviors are explicitly needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-orchard-tree-counting)
- [Artifact README](artifact/README.md)
- [Artifact CHANGELOG](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with Python CLI commands; CLI execution writes GeoTIFF and JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primary files include result.tif, tree_stats.json, and output-manifest.json.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
