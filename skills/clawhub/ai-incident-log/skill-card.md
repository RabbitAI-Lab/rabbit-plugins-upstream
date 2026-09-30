## Description:

Records AI mistakes, hallucinations, and other incidents in a local JSONL ledger and provides incident lists and summary reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory all rights reserved

## Use Case:

Developers and operations teams use this skill to document AI incidents, track corrective actions, and review incident trends for follow-up. It does not replace professional or regulatory judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incident descriptions may expose sensitive operational information in the local ledger.

Mitigation: Store the ledger in an appropriate local location and avoid recording secrets or regulated data.

Risk: A remote installation may retrieve unverified source code.

Mitigation: Verify the remote source and tag before using the remote installation command.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-incident-log)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [JSONL files, Text, JSON]

**Output Format:** [Local JSONL incident ledger; text incident lists and reports, or a JSON summary report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records include time, severity, model, description, action, and owner; reports summarize severity, model, and pending review.]

## Skill Version(s):

1.0.3 (source: server-resolved ClawHub release; packaged SKILL.md says 1.1.0 and manifest.json says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
