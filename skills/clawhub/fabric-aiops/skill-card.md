## Description:

Helps network operators inspect controller-managed fabrics, investigate health and configuration drift, and perform supported device and network changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network operators and engineers use this skill to review fabric health, investigate degraded WAN links and configuration drift, and make supported controller changes. Meraki supports the broadest read/write coverage; other platforms have narrower coverage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable controller access can make disruptive live changes; the skill has no enforced read-only mode or approval gate.

Mitigation: Use least-privilege, preferably read-only controller accounts by default; authorize each write separately and preview supported changes with dry-run.

Risk: Exposed credentials or untrusted controller endpoints can put the fabric at risk.

Mitigation: Restrict MCP hosts, avoid long-lived master passwords in environment variables where possible, and review local audit and undo records after use.

Risk: Controller integrations may behave differently in live environments because coverage has not been fully exercised against live controllers.

Mitigation: Verify read results and test planned changes in a controlled environment before production use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/fabric-aiops)
- [Project homepage (listed in skill metadata; not verified as release provenance)](https://github.com/AIops-tools/Fabric-AIops)
- [Capabilities](references/capabilities.md)
- [Agent guardrails](references/agent-guardrails.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Shell commands, Guidance]

**Output Format:** [Text, Markdown, and structured JSON from controller tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings may be ranked; supported changes can be previewed before execution.]

## Skill Version(s):

0.12.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
