## Description:

Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can turn articles, reports, papers, notes, or outlines into visually unified, image-based PowerPoint presentations. The skill is suited to decks where each slide can be a single generated image rather than individually editable text and shapes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API-key check may expose the dLazy API key if a service connection redirects or uses an unencrypted connection.

Mitigation: Do not use until the maintainer safely handles redirects and blocks unencrypted connections; verify the configured service endpoint.

Risk: Source material and images are sent to dLazy for processing; generation uses dLazy credits, and shared API configuration persists locally.

Mitigation: Send only material approved for external processing, review dLazy's image protections and retention practices, monitor credit use, and protect shared local configuration.

## Reference(s):

- [Project repository (metadata homepage)](https://github.com/dlazy-ai/ai-ppt-slides)

## Skill Output:

**Output Type(s):** [Files, Guidance]

**Output Format:** [Generated 16:9 slide images assembled into an image-based PowerPoint (.pptx), with optional speaker notes and supporting project files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3 and a dLazy API key. Optional settings include the dLazy base URL, image model, and runtime home. Slide text and graphics are part of each image rather than individually editable objects.]

## Skill Version(s):

1.0.24 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
