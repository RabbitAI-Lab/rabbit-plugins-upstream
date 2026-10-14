## Description:

Selects a dLazy image model for a prompt and generates images through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to select and run image-generation models for prompts, optionally using reference images or enhancing generated assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and provided media files may be sent to dLazy's hosted service.

Mitigation: Review prompts and files for sensitive content before submission.

Risk: Authentication can store an API key locally.

Mitigation: Use DLAZY_API_KEY per command if local key storage is undesirable, and rotate or revoke keys when needed.

Risk: A global CLI installation adds third-party software to the local environment.

Mitigation: Review the pinned CLI package before installation, or use the pinned npx command on demand.

## Reference(s):

- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Image URLs]

**Output Format:** [Text with shell commands and links to generated assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are hosted by dLazy.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata; skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
