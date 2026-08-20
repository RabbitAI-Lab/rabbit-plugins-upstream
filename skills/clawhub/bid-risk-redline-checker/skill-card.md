## Description:

Assists agents with bid risk checks by identifying restrictive tender clauses, redline signals, buyer supplier patterns, comparable awards, and bid decision recommendations from Zhiliaobiaoxun bid data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External business users and procurement teams use this skill through an agent to evaluate a specific tender for bid/no-bid risk, competition openness, likely competitors, price anchors, and recommended next actions. The skill is intended for evidence-backed decision support using public bid and award data, not for making factual accusations about organizations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports may preserve signed detail links that can grant access when shared.

Mitigation: Share Markdown or HTML reports only with intended recipients, and review report links and citation details before distributing them.

Risk: The skill can create a device-based account and persist an API key locally when no preconfigured key is available.

Mitigation: Prefer a preconfigured ZLBX_API_KEY when possible; if auto-registration is used, confirm user consent first and remove ~/.zlbx/config.json when the credential is no longer needed.

Risk: Bid, project, and company queries are sent to the Zhiliaobiaoxun API.

Mitigation: Use the skill only when sending those query terms to the Zhiliaobiaoxun service is acceptable for the user's project and organization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/bid-risk-redline-checker)
- [Workflow guide](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Report template](references/report-template.md)
- [Auto-registration flow](references/auto-register.md)
- [HTML report renderer](scripts/render_report.py)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown decision report with an optional self-contained HTML report file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include cited bid/company records when available and may preserve signed detail links returned by the API.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
