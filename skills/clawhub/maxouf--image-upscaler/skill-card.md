## Description:

Guides agents in choosing and running image upscaling with cloud services or local Real-ESRGAN, optionally including face restoration and batch output tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxouf](https://clawhub.ai/user/maxouf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users processing individual images or batches use this skill to choose an upscaling route, enhance images to a larger size, optionally restore faces, and receive output URLs and status details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, URLs, and dataset fields may be sent to external processing services, and share-link permissions can expose source files more broadly.

Mitigation: Review service data handling and link permissions before processing; use local Real-ESRGAN for images that must stay on-device.

## Reference(s):

- [Skill homepage](https://github.com/maxouf/sherwood-skills/tree/main/skills/image-upscaler)
- [Gotchas: image upscaling cost and recovery](references/gotchas.md)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Files]

**Output Format:** [Markdown with inline shell commands, JSON examples, and CSV output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Batch results include an output URL, dimensions, and status for each image; CSV can preserve selected source fields.]

## Skill Version(s):

1.0.0 (source: frontmatter; matches server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
