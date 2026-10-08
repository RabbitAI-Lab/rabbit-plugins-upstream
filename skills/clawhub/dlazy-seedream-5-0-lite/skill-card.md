## Description:

Generates images from text prompts or reference images using Doubao Seedream 5.0 Lite.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from prompts or transform reference images through the dLazy Seedream service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any referenced local media files are sent to dLazy services.

Mitigation: Review prompts and reference files before submission; avoid sending sensitive content.

Risk: CLI login or key setup stores an API key in local configuration.

Mitigation: Use a per-invocation DLAZY_API_KEY if local key storage is unwanted.

Risk: Running the pinned third-party CLI executes an external package.

Mitigation: Review the pinned @dlazy/cli package and its source before installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy CLI repository (listed in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return generated image URLs or asynchronous task IDs; images may be downloaded locally.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata; artifact frontmatter: 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
