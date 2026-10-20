## Description:

Helps agents generate and edit images from text prompts and reference images using Nano Banana 2.0 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images from prompts and optional reference images with a dLazy account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media are sent to dLazy's hosted service.

Mitigation: Do not submit sensitive prompts or images without authorization.

Risk: Image generation may consume paid credits.

Mitigation: Check the estimated cost with --dry-run before generating.

Risk: The CLI stores an API key in local configuration.

Mitigation: Protect the configuration and rotate or revoke the key when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return image URLs or an asynchronous task identifier; saving an image locally is optional.]

## Skill Version(s):

1.3.31 (source: ClawHub release; bundled skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
