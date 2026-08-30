## Description:

ODSH-Interop helps an OpenClaw agent decide whether to handle an operator request itself or relay heavier execution work to a DeepSeek Harness execution layer using bridge envelopes, shared zones, notifications, and optional audit-ledger queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mikoribbit](https://clawhub.ai/user/mikoribbit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw operators use this skill to route requests between conversational handling and an external DSH execution layer, especially for file, code, batch, network, and optional desktop automation work. It also guides creation of bridge task envelopes and read-only health queries against the optional SQLite audit ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad automatic delegation can send files, commands, network work, or enabled desktop automation to an always-ready DSH execution layer.

Mitigation: Install only when that routing behavior is intended, and ask for explicit confirmation before relaying sensitive, account, credential, financial, or desktop-control tasks.

Risk: The shared bridge directory, notification channel, DSH daemon, and optional Cua desktop automation setup form a trust boundary for relayed execution.

Mitigation: Confirm those components are trusted and correctly configured before relying on the bridge for execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mikoribbit/skills/odsh-interop)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON envelope examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce bridge task envelopes and read-only audit queries; relayed execution depends on a trusted shared bridge, notification channel, DSH daemon, and optional desktop automation setup.]

## Skill Version(s):

1.2.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
