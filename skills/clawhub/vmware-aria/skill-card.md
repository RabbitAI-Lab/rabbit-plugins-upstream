## Description:

Helps agents investigate VMware Aria Operations metrics, alerts, capacity, anomalies, and reports, with limited administrative actions when authorized.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and engineers use this skill to inspect VMware Aria Operations monitoring data, investigate alerts, assess capacity, and generate reports. Authorized users can also manage alerts, definitions, reports, and maintenance state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized write actions can alter alerts, reports, definitions, or resource maintenance state.

Mitigation: Use a read-only service account by default; expose only needed write tools and require approval before changes.

Risk: Aria credentials may be exposed if stored in a plaintext password file.

Mitigation: Prefer a secret manager or process environment over a plaintext .env file.

Risk: Disabling TLS verification or skipping authentication checks can mask insecure or unverified connectivity.

Mitigation: Keep TLS verification enabled and do not treat --skip-auth as proof of authentication or production readiness.

## Reference(s):

- [Project homepage (skill metadata)](https://github.com/vmware-skills/VMware-Aria)
- [Capabilities](references/capabilities.md)
- [Agent guardrails](references/agent-guardrails.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational text or Markdown with monitoring findings and optional command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize Aria Operations results and recommend follow-up actions; administrative changes require authorization.]

## Skill Version(s):

2.4.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
