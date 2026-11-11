## Description:

Enhances image clarity and detail with super-resolution and returns an enhanced image URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People restoring or enlarging low-resolution images can use this skill to submit an image for super-resolution and receive an enhanced image URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial and noted CLI login and authentication steps that did not match the stated image-enhancement purpose.

Mitigation: Before installing, confirm the login and authentication steps fit your needs and review the CLI and its credential handling through a trusted source.

Risk: The documented workflow sends provided parameters and local image files to dLazy-hosted services.

Mitigation: Submit only images and details you are comfortable sending to the service.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Image URL, JSON]

**Output Format:** [JSON containing the enhanced image URL and output metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return a task identifier for asynchronous jobs; the result image can optionally be saved to a local path.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
