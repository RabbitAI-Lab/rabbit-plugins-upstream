## Description:

Extracts a source video's first frame and audio, uses video understanding to generate a prompt, and returns a Seedance 2.0 replication bundle with first-frame, audio, and video outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's pinned CLI for video replication workflows. It is used when an agent needs to send selected source video media to dLazy, generate a replication prompt, and receive hosted output assets or asynchronous task status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected media and prompts to dLazy's hosted API and media storage.

Mitigation: Use only media and prompts appropriate for dLazy processing, and confirm organizational data-sharing requirements before invocation.

Risk: Authentication uses a dLazy API key stored in local CLI configuration or supplied through the environment.

Mitigation: Use the documented login or auth command, keep the key scoped to the intended organization, and rotate or revoke it from the dLazy dashboard when needed.

Risk: Global npm installation persists a CLI binary on the system.

Mitigation: Prefer the pinned npx invocation for temporary use, review the linked source or npm package before installing, and avoid running npm as an administrator.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with bash examples and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs, downloaded files when --save is used, or asynchronous task identifiers when --no-wait is used.]

## Skill Version(s):

1.3.14 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
