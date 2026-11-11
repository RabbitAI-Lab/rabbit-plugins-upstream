## Description:

Uses Recraft V4 Vector to generate vector graphics from text prompts for logos, icons, and scalable design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers can create vector graphics such as logos and icons from text prompts, then use the generated asset in design workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any supplied local media files are sent to dLazy-hosted services for generation.

Mitigation: Avoid sending sensitive content unless you are comfortable with dLazy handling it.

Risk: The skill requires dLazy CLI sign-in and API key setup; the security review noted that this authentication flow was not clearly matched to the stated graphics purpose.

Mitigation: Review the CLI and service requirements before use, keep the API key private, and rotate or revoke it if needed.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [Generated vector graphic assets with a JSON response containing result URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a prompt; aspect ratio is optional; output can be saved to a local path.]

## Skill Version(s):

1.3.37 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
