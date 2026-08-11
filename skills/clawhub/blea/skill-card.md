## Description:

Use BLEA to diagnose and automate local Bluetooth Low Energy devices with scans, GATT reads, bounded notifications, read-only captures, offline diffs and replay, guarded exchanges, guarded writes, and repeatable YAML workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nitmi](https://clawhub.ai/user/nitmi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect nearby BLE devices, collect structured evidence, compare or replay captures offline, and prepare guarded local commands for authorized diagnostics or automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: BLE write operations can change device state when the device, characteristic, payload, or expected effect is wrong.

Mitigation: Review every write operation, require user authorization, use the exact resolved device identifier, enable the BLEA write guard, and prefer read-back or notification verification.

Risk: Capture files may contain nearby-device identifiers or raw BLE data.

Mitigation: Redact identifiers before sharing captures and treat .blea.jsonl files as sensitive evidence.

Risk: Hosted agents may not have local Bluetooth adapter access, so prepared commands can be mistaken for executed diagnostics.

Mitigation: Clearly label commands that were prepared but not executed and report live scan, connection, read, notification, or write results only when structured BLEA output is available.

## Reference(s):

- [BLE safety policy](references/safety.md)
- [BLEA workflow YAML](references/workflows.md)
- [Evidence Format v1](https://github.com/Nitmi/blea/blob/v0.6.1/docs/evidence-format-v1.md)
- [Diff Format v1](https://github.com/Nitmi/blea/blob/v0.6.1/docs/diff-format-v1.md)
- [Replay Format v1](https://github.com/Nitmi/blea/blob/v0.6.1/docs/replay-format-v1.md)
- [Platform Acceptance](https://github.com/Nitmi/blea/blob/v0.6.1/docs/platform-acceptance.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, YAML snippets, and JSON or JSONL evidence references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May prepare commands for a local BLE host or analyze uploaded .blea.jsonl evidence; live BLE results require corresponding structured tool or CLI output.]

## Skill Version(s):

0.6.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
