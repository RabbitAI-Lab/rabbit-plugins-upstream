## Description:

Use for direct Open Exchange Rates integration, plan-aware historical-rate retrieval, currency-conversion safeguards, and caller-owned App ID handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pontjs](https://clawhub.ai/user/pontjs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to integrate Open Exchange Rates through Pontx-local SDK or CLI workflows while keeping the App ID in the caller environment. It helps plan historical-rate and currency-conversion reads with preview, approval, quota, and financial-control safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Open Exchange Rates App ID could be exposed in chat, source control, command transcripts, or logs.

Mitigation: Keep the App ID in environment variables, use local SDK or CLI request construction, and show only redacted previews before approval.

Risk: Live exchange-rate reads may use an unsupported plan, exceed time-series limits, or consume unexpected quota.

Mitigation: Verify the current Pontx resource and plan, split historical reads into bounded monthly requests, select only required currencies, and estimate quota impact before execution.

Risk: Exchange-rate outputs could be used directly in financial transactions without local validation.

Mitigation: Treat rates as application input and apply the caller's financial validation, rounding policy, and approval controls before transaction use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pontjs/skills/pontx-open-exchange-rates)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline bash commands and implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include redacted previews, plan checks, quota estimates, and approval boundaries before live reads.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
