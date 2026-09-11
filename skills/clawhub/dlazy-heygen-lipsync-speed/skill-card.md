## Description:

HeyGen Lipsync Speed helps agents invoke dLazy's hosted HeyGen lip-sync model for fast video and audio synchronization workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent run dLazy CLI commands that submit video and audio inputs to a hosted lip-sync service and return generated results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party cloud service and can upload user-selected video, audio, or image files for processing.

Mitigation: Only provide media intended for upload to dLazy, and review organizational data-handling requirements before use.

Risk: The skill depends on a dLazy API key stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the key, prefer isolated environments for use, and rotate or revoke the key if exposure is suspected.

Risk: The skill requires npm or npx execution of the dLazy CLI.

Mitigation: Prefer the pinned on-demand npx command or an isolated environment, and review the referenced CLI source or package before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted generated media URLs, an async task generateId for polling, or a local saved asset path when --save is used.]

## Skill Version(s):

1.3.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
