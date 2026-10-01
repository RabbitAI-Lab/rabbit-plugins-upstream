## Description:

Helps agents screen text for safety and sensitive data, identify AI user agents, assess a site's accessibility to agents, and perform approved business operations through Overwing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frod27](https://clawhub.ai/user/frod27)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Overwing to review text before sharing or acting on it, assess claimed bot identities and site readiness, and carry out authorized operations in connected business systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text and context sent for evaluation may contain sensitive information and may be retained when using an API key.

Mitigation: Only send data approved for Overwing processing; use --no-store for sensitive evaluations and an evaluate-only key when possible.

Risk: Beacon checks and wallet-backed requests may incur charges.

Mitigation: Confirm the human has authorized a paid check or wallet spend before starting one.

Risk: Tower actions can change business records.

Mitigation: Use narrowly scoped agent keys, review capabilities and inputs, and honor pending human approvals; avoid wildcard scopes.

Risk: Optional MCP and SDK packages add dependencies to the agent environment.

Mitigation: Pin or separately review optional packages before running them.

## Reference(s):

- [Overwing](https://overwing.ai)
- [Overwing API documentation](https://overwing.ai/docs)
- [Overwing agent guide](https://overwing.ai/llms.txt)
- [Overwing Atlas](https://overwing.ai/atlas)
- [Overwing skill on ClawHub](https://clawhub.ai/frod27/skills/overwing)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown guidance and JSON service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Text checks return a verdict, recommended action, and per-rule results; Beacon reports site findings, and Tower returns action decisions and receipts.]

## Skill Version(s):

1.6.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
