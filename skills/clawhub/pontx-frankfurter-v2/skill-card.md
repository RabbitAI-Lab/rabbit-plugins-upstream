## Description:

Integrate Frankfurter v2 through Pontx for reference-rate conversion, provider-pinned compliance, auditable time series, attribution, and large exports. Use for FX or central-bank rate tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pontjs](https://clawhub.ai/user/pontjs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to integrate Frankfurter v2 reference exchange-rate retrieval through Pontx for display conversion, provider-pinned compliance calculations, auditable time series, attribution retention, and large exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents toward live exchange-rate retrieval through Pontx.

Mitigation: Review the previewed request and approve live retrieval only when the provider, date range, and intended use are correct.

Risk: Compliance or accounting calculations can be wrong if the required provider or jurisdiction is omitted or silently substituted.

Mitigation: Provide the controlling provider or jurisdiction, retain returned observation details, and do not replace missing provider-specific observations with blended rates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pontjs/skills/pontx-frankfurter-v2)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell commands and code-oriented guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to preview live requests, require explicit approval before retrieval, and preserve returned observation context.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
