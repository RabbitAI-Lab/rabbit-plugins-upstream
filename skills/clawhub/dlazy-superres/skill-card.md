## Description:

Image super-resolution tool: enhances image clarity and details, returning enhanced URL, suitable for low-res asset restoration and upscaling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Users and creative professionals can upscale low-resolution images to improve clarity and detail, then retrieve the enhanced image URL or save the result locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images provided for processing are uploaded to dLazy's service.

Mitigation: Send only images you are comfortable sharing with dLazy.

Risk: The CLI stores an API key locally and API use may incur charges.

Mitigation: Protect the saved key, rotate or revoke it when needed, and review cost information before running requests.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-superres)

## Skill Output:

**Output Type(s):** [Image, URL, JSON]

**Output Format:** [JSON result with an enhanced image URL and image metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return an asynchronous task identifier or save the resulting image to a local path.]

## Skill Version(s):

1.3.38 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
