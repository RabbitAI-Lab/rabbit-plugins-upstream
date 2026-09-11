## Description:

Helps users discover early procurement opportunities by scanning proposed projects, purchase intents, and expiring contracts, then ranking leads with recommended next actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business development teams use this skill to scan China-focused early procurement and project signals by industry, product, region, and budget. It helps prioritize follow-up before formal tenders are published.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports and result links may include sk-bearing URLs that can grant access to whoever has them.

Mitigation: Treat generated HTML reports and signed links as sensitive and share them only with intended recipients.

Risk: Automatic registration transmits a stable device fingerprint for trial-account de-duplication.

Mitigation: Prefer a user-provided ZLBX_API_KEY when available and require user consent before automatic registration.

Risk: Procurement lead rankings may be affected by incomplete, delayed, or unavailable source data.

Mitigation: Keep source dates and data gaps visible, and verify amounts, dates, and organization names before business decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/proposed-project-tracker)
- [Workflow guide](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Auto-registration flow](artifact/references/auto-register.md)
- [Report template](artifact/references/report-template.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown opportunity lists with optional self-contained HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY; generated reports and result links can include signed access URLs.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
