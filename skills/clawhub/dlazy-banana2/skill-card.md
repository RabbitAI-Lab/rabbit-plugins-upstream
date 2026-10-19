## Description:

Generate or edit images from text prompts and optional reference images with Nano Banana 2.0 through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images from prompts and reference images through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media may be uploaded to dLazy's hosted service.

Mitigation: Only submit prompts and files approved for third-party processing.

Risk: Login can save an API key in local CLI configuration.

Mitigation: Protect local credentials; use a per-invocation key where appropriate and rotate or revoke exposed keys.

Risk: Image generation may consume paid credits.

Mitigation: Review the cost estimate with the CLI's dry-run option before submitting requests.

Risk: The optional save command writes output to a chosen local path.

Mitigation: Confirm the destination before saving generated files.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Images]

**Output Format:** [CLI JSON response with image URLs; optional saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID instead of an immediate image.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
