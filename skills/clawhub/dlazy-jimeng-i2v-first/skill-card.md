## Description:

Generate dynamic videos from a single first-frame image and a prompt using Jimeng.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn a still image and a text prompt into a Jimeng video through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The prompt and supplied image are sent to dLazy services, and local image files are uploaded for generation.

Mitigation: Only submit media and prompts you are comfortable sharing with dLazy.

Risk: The CLI can save an API key in the local user configuration.

Mitigation: Protect the stored key, or provide DLAZY_API_KEY for an invocation and rotate or revoke exposed keys.

Risk: Video generation may incur usage costs.

Mitigation: Review the cost estimate before requesting generation.

Risk: The examples use --image while the listed option is --firstFrame.

Mitigation: Check dlazy jimeng-i2v-first -h and use the option shown by the installed CLI.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key management](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Video, JSON, Shell commands, Guidance]

**Output Format:** [Generated video asset with JSON task status and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 5- or 10-second clips; asynchronous runs may return a task ID.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
