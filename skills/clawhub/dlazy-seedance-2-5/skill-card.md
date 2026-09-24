## Description:

ByteDance's next-generation video model: up to 30 seconds per clip with native 4K, substantially better instruction following and long-form narrative, multi-modal references, and first/last frame control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate video assets through the dLazy Seedance 2.5 CLI, including prompt-only generation, multi-modal reference generation, and first/last-frame controlled generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media paths provided to the skill may be sent to dLazy's hosted API and uploaded to dLazy media storage.

Mitigation: Avoid passing private media unless the user is comfortable sending it to dLazy's hosted service.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use the per-run DLAZY_API_KEY environment variable when persistent local credential storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: A global CLI install persists tooling on the user's system.

Mitigation: Prefer the pinned npx invocation when the user does not want a persistent global install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with CLI commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs or an asynchronous task identifier for later polling.]

## Skill Version(s):

1.2.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
