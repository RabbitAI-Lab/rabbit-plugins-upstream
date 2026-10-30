## Description:

Gives your agent hands through Zambo, the verifiable work layer for AI, with 153 tools behind one remote MCP endpoint. Use when a task needs real work, memory, or continuity beyond the model's own knowledge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zambodotdev](https://clawhub.ai/user/zambodotdev)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use an agent with Zambo to run multi-step research or analysis, save and recall memory, and hand work across sessions or agents with receipts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private code or conversation context shared with remote tools may expose sensitive information.

Mitigation: Send sanitized, narrowly scoped inputs; review Zambo's privacy policy and sharing settings before sharing private material.

Risk: A published handover may contain private information that automatic redaction misses, and withdrawing it cannot recall downloaded copies.

Mitigation: Inspect handovers before publication and remove sensitive details; treat receipt verification as integrity checking, not confidentiality protection.

## Reference(s):

- [Zambo agent documentation](https://zambo.dev/.well-known/llms.txt)
- [Zambo installation guide](https://zambo.dev/install)
- [HANDOVER guidance](https://zambo.dev/handover/)
- [Receipt verification](https://zambo.dev/verify/)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Code, Structured results, Guidance]

**Output Format:** [Varies by task; text, Markdown, code, structured results, and verifiable receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include AER-1 receipts or HANDOVER links.]

## Skill Version(s):

1.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
