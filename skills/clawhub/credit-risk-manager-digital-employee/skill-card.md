## Description:

Provides a credit-risk management workflow for industry rule generation, large-exposure management, credit-policy analysis, risk collaboration, risk information extraction, post-loan monitoring, post-loan management, and multimodal verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Bank credit-risk, post-loan, and risk-management professionals use this skill to structure credit-risk information, generate industry review rules, analyze policy context, monitor large exposures and post-loan risk, and draft human-reviewed risk and antifraud reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide work involving sensitive lending, customer, credit-bureau, payment-flow, and financial data.

Mitigation: Use it only in a governed financial environment with approved connectors, role-based access, and institution-defined limits for sensitive data.

Risk: The skill describes credit recommendations, internal API use, report archival, customer classification changes, and disposal actions.

Mitigation: Require explicit human approval and separate monitored authorization before any credit action, internal system call, archival step, classification change, or disposal action.

Risk: Audit logs and generated reports may contain regulated or confidential financial information.

Mitigation: Store audit logs and reports only in institution-approved locations with approved retention, access-control, encryption, and redaction controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gechengling/skills/credit-risk-manager-digital-employee)
- [Publisher profile](https://clawhub.ai/user/gechengling)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown and JSON reports, rules, checklists, and human-reviewed recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory and require qualified human review before any credit, lending, or operational action.]

## Skill Version(s):

2.0.3 (source: server release metadata; artifact frontmatter lists 2.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
