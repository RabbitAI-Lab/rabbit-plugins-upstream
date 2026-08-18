## Description:

Generate dynamic videos from a first-frame image and prompt using Jimeng through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create short image-to-video generations from a supplied first-frame image and prompt through dLazy/Jimeng.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media paths supplied to the CLI can be uploaded to dLazy services for generation.

Mitigation: Use the skill only with content that may be processed by dLazy/Jimeng and avoid submitting sensitive media or prompts unless approved.

Risk: Authentication can save a dLazy API key in the local CLI configuration.

Mitigation: Prefer per-invocation credentials or rotate and revoke keys from the dLazy dashboard when access is no longer needed.

Risk: A global CLI install persists tooling on the user system.

Mitigation: Use the pinned npx invocation or review the pinned CLI source before choosing a global install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return generated media URLs or an asynchronous generateId for polling.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
