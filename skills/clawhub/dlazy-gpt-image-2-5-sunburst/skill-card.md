## Description:

Generates and edits detailed images with GPT Image 2.5 Sunburst, including reference images, aspect ratios up to 21:9, and quality settings up to max.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and designers can generate or edit images from prompts and reference images when fine detail, in-image text, or composition matters. The skill supports multiple aspect ratios and quality settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference files may be sent to dLazy, and local media files may be uploaded to its storage service.

Mitigation: Submit only prompts and reference files you are comfortable uploading to dLazy.

Risk: Image generation may consume paid credits, and the CLI stores an API key in its local configuration.

Mitigation: Review the pinned CLI before installing, protect the saved API key, and rotate or revoke it if needed.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, Files, API Calls]

**Output Format:** [Generated image files (PNG) returned by URL or saved locally, with JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports prompt-based generation and image editing with up to five reference images; output can be returned asynchronously.]

## Skill Version(s):

1.2.24 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
