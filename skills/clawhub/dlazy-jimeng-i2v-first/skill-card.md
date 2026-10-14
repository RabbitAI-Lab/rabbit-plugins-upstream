## Description:

Guides agents to generate a video from a first-frame image and text prompt using Jimeng through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent through image-to-video generation from a first-frame image and prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images are uploaded to dLazy, and prompts and parameters are sent to its hosted API.

Mitigation: Share only images and prompts approved for third-party processing.

Risk: Authentication may save an API key on the local machine.

Mitigation: Protect the local key and revoke or rotate it if exposed.

Risk: Documented options and sample output are inconsistent with the stated video workflow.

Mitigation: Check the command help and try a dry run before submitting a paid request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy CLI source (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with command examples and JSON result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned as a hosted link; asynchronous requests may return a task ID.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
