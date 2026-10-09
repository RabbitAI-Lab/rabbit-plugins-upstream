## Description:

Selects a dLazy image model based on the prompt and generates images through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate and refine images from text prompts or reference images with dLazy-hosted models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and generation parameters are sent to dLazy's cloud service.

Mitigation: Avoid including sensitive information in prompts or parameters.

Risk: Local media supplied as input can be uploaded to dLazy's media storage.

Mitigation: Review and authorize input files before supplying their paths.

Risk: Login stores a dLazy API key locally.

Mitigation: Protect the local credential; rotate or revoke the key through the dLazy dashboard if needed.

Risk: A global CLI installation persists on the user's system.

Mitigation: Use the pinned npx invocation if a persistent global install is not desired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Shell commands, Image URLs, Guidance]

**Output Format:** [Markdown guidance and CLI JSON responses with hosted image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is hosted by dLazy.]

## Skill Version(s):

1.3.27 (source: ClawHub release; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
