## Description:

Use when diagnosing KWDB incidents from logs, metrics, or system evidence, especially crashes, OOM, slow SQL, restarts, and cluster-wide availability symptoms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kwdb](https://clawhub.ai/user/kwdb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support engineers use this skill to triage KWDB incidents from logs, metrics, system evidence, SQL evidence, and optional source code. It guides diagnosis of functional failures, performance issues, mixed incidents, and cluster-level availability symptoms while keeping conclusions tied to available evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incident materials can contain sensitive logs, SQL text, object names, process arguments, metrics, secrets, or customer-specific details.

Mitigation: Redact secrets and customer-specific details before pasting evidence into chats, tickets, or generated reports, and limit access to the evidence and outputs.

Risk: The skill is designed to answer in Chinese, which can be unsuitable for teams that cannot review Chinese diagnostic output.

Mitigation: Install it only for teams comfortable reviewing Chinese incident analysis or route output through an approved translation and review process.

Risk: A diagnosis may be incomplete when fault time, evidence roots, metrics, SQL text, node logs, or source access are missing.

Mitigation: Use the intake gate to request the smallest missing evidence set and keep unsupported conclusions explicitly partial.

## Reference(s):

- [KWDB Troubleshooting Skill Page](https://clawhub.ai/kwdb/skills/kwdb-troubleshooting)
- [Official KWDB Source Repository](https://gitee.com/kwdb/kwdb)
- [Key Rules](artifact/references/key-rules.md)
- [Intake Gate](artifact/references/intake-gate.md)
- [Path Discovery](artifact/references/path-discovery.md)
- [Triage Playbook](artifact/references/triage-playbook.md)
- [Fault Localization Chain](artifact/references/fault-localization.md)
- [Evidence Rules](artifact/references/evidence-rules.md)
- [Output Modes](artifact/references/output-modes.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, guidance]

**Output Format:** [Chinese Markdown diagnostic report with optional inline shell commands and source-path references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Diagnosis-only output; unknown fields are marked as 待补充, and recovery, repair, decommission, and reproduction plans are excluded unless the user has provided confirmed reproduction details for a requested template.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
