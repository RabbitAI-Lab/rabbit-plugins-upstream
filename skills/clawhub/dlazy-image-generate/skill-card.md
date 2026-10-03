## Description:

Selects a dLazy image model for a prompt and guides image generation through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to choose an image-generation model and generate or edit images from text prompts and optional reference media via dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media may be sent to dLazy's hosted service.

Mitigation: Share only prompts and files approved for upload to that service.

Risk: An API key may be saved locally, and requests may consume credits.

Mitigation: Use a per-invocation key when persistent storage is unsuitable, protect credentials, and review available credits before large runs.

Risk: Installing the CLI introduces an external npm package.

Mitigation: Review the pinned package and its source before global installation in sensitive environments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI repository (declared in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance and generated image URLs returned in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May link to images hosted by dLazy.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
