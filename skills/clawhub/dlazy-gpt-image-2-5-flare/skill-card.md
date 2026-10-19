## Description:

Generates and edits images from text prompts and reference images through the dLazy hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images from prompts and optional reference images for everyday content workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the CLI requires trusting the dLazy npm package and hosted service.

Mitigation: Review the package and service before installation.

Risk: Prompts and referenced media are sent to dLazy cloud endpoints.

Mitigation: Avoid submitting sensitive prompts or media without authorization.

Risk: Login may store an API key in a local configuration file.

Mitigation: Protect local credentials and rotate or revoke the key if exposed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)
- [dLazy CLI project (linked in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Image URLs, JSON responses, Image files]

**Output Format:** [JSON response with hosted image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional asynchronous task ID; up to five reference images]

## Skill Version(s):

1.2.20 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
