## Description:

Analyzes a company from a bid-award perspective, using Zhiliaobiaoxun data to produce company intelligence reports, competitor analysis, and two-company comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users, procurement teams, sales teams, and competitive-intelligence analysts use this skill to evaluate a company through public bidding records, award history, customer and supplier relationships, competitor overlap, and public risk signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company-query data is sent to the Zhiliaobiaoxun service during analysis.

Mitigation: Use the skill only for queries you are comfortable sending to that service, and avoid sensitive internal deal names or confidential planning details unless policy permits.

Risk: Automatic registration collects a stable MAC-derived device hash and stores an API key locally.

Mitigation: Set ZLBX_API_KEY yourself to skip automatic registration, require user consent before registration, and review permissions on ~/.zlbx/config.json after setup.

Risk: Generated HTML reports and embedded links may point to unexpected destinations if the underlying data is unexpected.

Mitigation: Treat generated report links as untrusted unless the destination is expected, and keep API-returned source links intact for traceability.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/bid-award-competitive-analysis)
- [API quick reference](artifact/references/api-quick.md)
- [Seven-step workflow](artifact/references/workflow.md)
- [Automatic registration flow](artifact/references/auto-register.md)
- [Report template](artifact/references/report-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown report with optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved automatic registration; reports may include source links returned by the service.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
