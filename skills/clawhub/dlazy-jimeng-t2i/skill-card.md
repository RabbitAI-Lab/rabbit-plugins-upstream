## Description:

Generates images from text prompts with Jimeng through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from text prompts, optionally supplying reference images and downloading the result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media may be sent to dLazy, and generated images are hosted there.

Mitigation: Avoid submitting sensitive prompts or files unless the hosted service is appropriate for them.

Risk: Generation requests may consume paid credits.

Mitigation: Check the cost estimate with the documented dry-run option before generating.

Risk: Logging in can save an API key locally.

Mitigation: Use the documented environment-variable option when local credential persistence is undesirable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI source and documentation](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown instructions and JSON image-result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be downloaded locally; hosted image URLs are returned by dLazy.]

## Skill Version(s):

1.3.31 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
