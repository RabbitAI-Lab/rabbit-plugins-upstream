## Description:

Generates images from text prompts with Jimeng through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request Jimeng-generated images from text prompts, optionally using reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media may be sent to dLazy's hosted service.

Mitigation: Avoid sending sensitive prompts or files; review inputs before invoking the CLI.

Risk: Authentication may save an API key in local CLI configuration.

Mitigation: Protect local credentials and rotate or revoke the key if exposed.

Risk: Generation requests may consume account credits.

Mitigation: Check estimated costs with dry-run before making paid requests.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Image URLs]

**Output Format:** [JSON response with generated image URLs; optionally a saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID for later polling.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
