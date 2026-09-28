## Description:

Generates and edits images with Nano Banana Pro from text prompts and reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images from prompts and optional reference images through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the hosted service requires a dLazy API key that may be stored locally or passed to the CLI.

Mitigation: Use a key only when comfortable with the service and protect locally stored credentials.

Risk: Prompts and selected local image files are sent to dLazy's hosted service.

Mitigation: Confirm the provider is intended and review files before uploading them.

Risk: Generation may spend applicable dLazy credits.

Mitigation: Check expected cost and available credits before running requests.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON containing hosted image URLs; optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID before the image is ready.]

## Skill Version(s):

1.2.25 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
