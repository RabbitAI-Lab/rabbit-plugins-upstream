## Description:

Runs a local multi-criteria geospatial suitability analysis pipeline with factor standardization, AHP or entropy weighting, weighted overlay, and suitability classification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers, GIS analysts, and geospatial engineers use this skill to run suitability analysis from local raster input or synthetic data and produce scored, classified suitability outputs with summary metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package security review found under-disclosed network, download, cache, and credential-handling helpers, including hardcoded Earthdata credentials.

Mitigation: Review the package before installing it in environments with sensitive credentials or private location queries; remove or clearly document the helper modules and delete and rotate the hardcoded credentials before approval.

Risk: The package has unpinned runtime dependencies.

Mitigation: Pin and review dependencies before deployment in controlled or production environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-suitability-analysis-framework)
- [README](README.md)
- [SKILL](SKILL.md)
- [CHANGELOG](CHANGELOG.md)
- [LICENSE](LICENSE)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands, Guidance]

**Output Format:** [GeoTIFF, GeoJSON, JSON, and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces suitability score rasters, suitability class rasters, statistics JSON, and an output manifest.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact CHANGELOG and openai.yaml list 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
