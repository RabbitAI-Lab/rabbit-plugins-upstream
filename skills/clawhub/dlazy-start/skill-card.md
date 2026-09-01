## Description:

Quickstart guidance for AI orchestrators using @dlazy/cli to install, authenticate, discover tools, invoke cloud and local media workflows, poll asynchronous tasks, and recover from common failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agent operators use this skill to drive @dlazy/cli safely and consistently, including capability discovery, command invocation, async task polling, and common failure recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An autonomous agent may use browser cookies for a download task without clear user consent, exposing browser session data.

Mitigation: Require explicit approval before any cookies_from_browser option is used, and limit consent to the specific download task.

Risk: API keys or saved CLI configuration may be exposed if agents use inline credentials or leave config files broadly readable.

Mitigation: Prefer device-code login, avoid inline API keys when possible, and keep ~/.dlazy/config.json permissions restricted.

Risk: Asset downloads could be saved to unintended locations when an agent chooses --save paths autonomously.

Mitigation: Require explicit approval for each --save destination before downloading generated assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [@dlazy/cli source link from skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to discover live CLI tools before invoking them and to parse machine-readable JSON envelopes where appropriate.]

## Skill Version(s):

2.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
