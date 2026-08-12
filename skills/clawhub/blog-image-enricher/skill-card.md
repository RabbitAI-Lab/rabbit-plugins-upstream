## Description:

Read a plain Markdown file, generate header and section images using OpenClaw's default image generation setup, create a new *_img.md copy with embedded PNGs, and store generated images in an img/ folder next to the original file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, writers, and documentation maintainers use this skill to create an image-enriched Markdown copy while preserving the original document. It is intended for Markdown files where each heading should receive a generated PNG and the resulting assets should be organized into a sibling img/ directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags that the skill tells an agent to read local OpenClaw runtime credential configuration for image generation.

Mitigation: Review before installing and prefer platform-provided image generation authentication that does not require the agent to read secret files directly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/blog-image-enricher)
- [Publisher profile](https://clawhub.ai/user/j3ffyang)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance for creating an enriched Markdown file with embedded PNG image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for a sibling *_img.md file and PNG assets under an img/ directory; image generation depends on the platform-provided image_generate tool and existing OpenClaw image configuration.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
