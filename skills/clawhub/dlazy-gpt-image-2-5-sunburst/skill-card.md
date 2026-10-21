## Description:

Generates and edits detailed images from text prompts and optional reference images through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images with detailed composition, in-image text, reference images, and adjustable aspect ratio and quality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local files may be uploaded to dLazy; generated results are hosted there.

Mitigation: Share only content appropriate for the third-party service and review its terms before use.

Risk: Logging in can store a dLazy API key locally.

Mitigation: Protect local credentials and rotate or revoke the key in the dLazy dashboard if needed.

Risk: A persistent global installation of the third-party CLI may be unnecessary.

Mitigation: Review the CLI before installing and prefer the pinned on-demand npx command when a global installation is not wanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-sunburst)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image URLs, Shell commands, Guidance]

**Output Format:** [JSON response with image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports up to five reference images, aspect ratios up to 21:9, and asynchronous generation.]

## Skill Version(s):

1.2.21 (source: ClawHub release metadata; bundled skill frontmatter: 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
