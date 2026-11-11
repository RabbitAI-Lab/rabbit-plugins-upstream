## Description:

Use for read-only on-premises Symantec EDR appliance, incidents, events, entities, threat feeds, policy lists and sandbox results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Security analysts and EDR administrators use it to inspect on-premises Symantec EDR appliances, incidents, events, entities, threat feeds, policy lists, and sandbox results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The separately installed software was unavailable for verification.

Mitigation: Verify the external package and select a reviewed version before supplying credentials.

Risk: Missing, partial, or unverified responses could be mistaken for healthy systems or zero findings.

Mitigation: Use a read-only appliance account and treat incomplete results as unknown; check verification status before drawing conclusions.

## Reference(s):

- [Agent guardrails](artifact/references/agent-guardrails.md)
- [Project homepage](https://github.com/AIops-tools/Symantec-EDR-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/symantec-edr-aiops)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Text responses with structured investigation records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only investigation results; treat missing, partial, and unverified results as unknown.]

## Skill Version(s):

0.1.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
