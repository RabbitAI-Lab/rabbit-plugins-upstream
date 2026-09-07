## Description:

Exports brand and social media design assets from an Ardot canvas into a controlled local asset library for governed distribution, provenance, and usage traceability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, design operations teams, and brand governance teams use this skill to export PNG and SVG design assets into a controlled local library, add provenance and license metadata, and maintain an auditable asset index for controlled distribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The export workflow writes downloaded and metadata-injected files to paths resolved from the local asset index.

Mitigation: Review _asset_index.json, the URL map, and the selected library root before running the scripts so files are written only to expected asset-library locations.

Risk: Optional model mode sends asset metadata prompts to a local service on port 8080.

Mitigation: Use template mode when model output is not needed, or run only a trusted local model service and review generated metadata statements before distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/asset-controlled-export-pipeline)
- [ClawHub publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with Python scripts, JSON configuration inputs, and generated or modified local asset files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports PNG and SVG asset download, metadata injection into PNG iTXt/XMP and SVG RDF, local index files, and optional localhost model-generated Chinese metadata statements.]

## Skill Version(s):

1.0.0 (source: frontmatter, manifest, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
