## Description:

Generate high-quality images with Doubao Seedream 4.5, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to call the dLazy CLI for Doubao Seedream 4.5 image generation from text prompts or reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local image paths supplied to the CLI may be uploaded to dLazy services for generation.

Mitigation: Avoid sending sensitive prompts or files unless the dLazy service terms and handling practices meet the user's requirements.

Risk: Authentication can persist an API key in the local dLazy CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY or npx when less local persistence is desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on a third-party CLI and hosted API.

Mitigation: Install only when the dLazy CLI and service are trusted, and review the pinned CLI package before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Guidance]

**Output Format:** [JSON result containing generated image URLs, with optional saved image files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async calls may return a generation ID for later polling.]

## Skill Version(s):

1.3.18 (source: server release evidence; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
