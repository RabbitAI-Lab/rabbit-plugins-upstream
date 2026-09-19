## Description:

Moonshot AI thinking model with text, image, and video understanding, suited to complex analysis, coding, and writing that needs long reasoning chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, writers, and other external users invoke this skill through the dLazy CLI to send prompts and optional image or video inputs to the hosted Kimi K3 model for analysis, coding assistance, and writing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local media paths may be sent to the dLazy hosted service for inference or upload.

Mitigation: Do not submit sensitive data unless the user accepts dLazy processing; review inputs before invocation.

Risk: Using CLI login can store an API key on disk in the user's dLazy configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials when less local persistence is desired, and rotate or revoke keys from the dLazy dashboard as needed.

Risk: Global installation persists a third-party CLI on the system.

Mitigation: Use the pinned npx command for on-demand execution or review the third-party CLI source before global installation.

Risk: Using --save can write generated output files to local paths.

Mitigation: Choose explicit save paths and review generated files before relying on or redistributing them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [JSON envelope containing generated outputs or async task status; generated content may be text, markdown, code, commands, configuration, or guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports prompt input, up to 10 images, up to 8 videos, dry-run cost estimates, async task IDs, polling, and optional local save paths.]

## Skill Version(s):

1.2.12 (source: server release evidence; artifact frontmatter and install spec reference 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
