## Description:

Records AI incidents in a local JSONL ledger and provides listing and summary reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theory: All rights reserved

## Use Case:

Developers and incident responders use this skill to record AI mistakes, hallucinations, or other incidents and review trends by severity and model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local incident ledger stores incident descriptions, models, actions, and owners in plaintext.

Mitigation: Choose a protected ledger location and do not record passwords, API keys, customer secrets, or regulated data.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-incident-log)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Plain-text listing or report, optional JSON report, and local JSONL incident ledger]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records include timestamp, severity, model, description, action, and owner.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
