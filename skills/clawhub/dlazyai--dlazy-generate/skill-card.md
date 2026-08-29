## Description:

Routes image, video, and audio generation requests to an appropriate dLazy CLI model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can use this skill to create images, videos, audio, and chained media workflows through dLazy-hosted generation models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media paths may be sent to dLazy cloud services for generation.

Mitigation: Use the skill only for data approved for dLazy processing, and avoid passing sensitive files or prompts.

Risk: Authentication may persist a dLazy API key in the user's local CLI configuration.

Mitigation: Use per-run DLAZY_API_KEY when persistent local credentials are not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Broad trigger terms may invoke dLazy for generic generation requests, including tasks involving files or paid credits.

Mitigation: Confirm dLazy use before execution when a request is ambiguous, file-bearing, or likely to consume credits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output from the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs hosted by dLazy services.]

## Skill Version(s):

1.3.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
