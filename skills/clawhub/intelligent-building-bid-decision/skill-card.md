## Description:

Analyzes low-voltage intelligent-building and security-monitoring bid opportunities using Zhiliaobiaoxun bid data to assess bid/no-bid posture, buyer history, likely competitors, pricing benchmarks, qualification thresholds, and bid-rejection risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, bid teams, and business development staff use this skill to evaluate a specific security-monitoring or intelligent-building tender, compare buyer history and likely competitors, and generate a traceable bid decision report with pricing guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports may preserve signed access links that can be shared outside the intended audience.

Mitigation: Review generated reports before distribution and remove or redact signed links when sharing outside the team.

Risk: The skill can persist account credentials for later API use.

Mitigation: Prefer a preconfigured API key managed by the user or organization, and protect any local credential file created for the skill.

Risk: Bid-search terms and optional registration device features are sent to the third-party provider.

Mitigation: Install and use the skill only when this provider-side data processing is acceptable, and require user consent before any automatic registration flow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/intelligent-building-bid-decision)
- [API Quick Reference](artifact/references/api-quick.md)
- [Bid Decision Workflow](artifact/references/workflow.md)
- [Report Template](artifact/references/report-template.md)
- [Auto Registration Flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown bid decision report, optional self-contained HTML report, and concise setup or follow-up guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports rely on API-returned evidence and may include signed access links when those links are returned by the data provider.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
