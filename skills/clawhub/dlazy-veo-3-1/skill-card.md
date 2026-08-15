## Description:

Generate high-quality cinematic effects videos with Google Veo 3.1, including text-to-video and image-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate videos through the dLazy CLI using Google Veo 3.1. It supports prompt-based generation, frame- or reference-image guided generation, and video extension through a hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files may be sent to dLazy's hosted service.

Mitigation: Confirm the hosted-service data flow is acceptable before use, and avoid submitting sensitive prompts or media unless approved.

Risk: Using the hosted generation API may consume dLazy account credits.

Mitigation: Use dry-run or review expected cost before generation when credit usage matters.

Risk: Authentication can save an API key in the local CLI configuration.

Mitigation: Use scoped keys, rotate or revoke keys from the dLazy dashboard when needed, or provide the key per invocation through the environment.

Risk: Global CLI installation persists a third-party command on the system.

Mitigation: Use the pinned npx invocation when a non-persistent install is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns hosted media URLs or asynchronous task status in JSON.]

## Skill Version(s):

1.3.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
