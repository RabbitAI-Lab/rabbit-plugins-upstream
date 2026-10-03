## Description:

Helps agents generate short videos from text or images using Google Veo 3.1 Fast through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short text-to-video or image-to-video generation through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media may be sent to dLazy's cloud service.

Mitigation: Share only prompts and media you are authorized to upload.

Risk: Generating videos may consume dLazy credits.

Mitigation: Check the cost estimate with the documented dry-run option before submitting a request.

Risk: Login stores an API key locally, and a global CLI install persists on the device.

Mitigation: Protect the local key and use the documented pinned npx invocation for on-demand CLI use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy CLI source (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI results can include hosted media URLs or asynchronous task identifiers.]

## Skill Version(s):

1.3.23 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
