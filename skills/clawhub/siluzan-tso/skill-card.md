## Description:

Routes advertising operations, campaign planning, account analysis, and market-report tasks through the Siluzan TSO CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing and advertising operators use this skill to manage supported ad accounts, plan campaigns, analyze performance, and prepare reports through Siluzan TSO. Campaign creation workflows are documented for Google and Meta.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled installers make broad persistent changes, invoke external installers, and register the skill across assistants.

Mitigation: Prefer the documented manual installation into one chosen skill directory; review installer behavior before using a bundled installer.

Risk: Onboarding may handle login credentials, identity details, or banking details through chat and command arguments.

Mitigation: Enter login credentials locally and use a secure onboarding route for identity and banking details.

Risk: Campaign changes can affect status, budgets, keyword matching, or deletion scope.

Mitigation: Review campaign status, budget, keyword matching, and deletion scope before approving changes.

## Reference(s):

- [Account and advertising workflows](references/core/workflows.md)
- [Analysis playbooks](references/core/playbooks.md)
- [Google Ads guide](references/google-ads/google-ads.md)
- [Account analytics guide](references/analytics/account-analytics.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Markdown, HTML, Spreadsheets]

**Output Format:** [CLI invocations, structured campaign data, and reports in HTML, Markdown, or XLSX]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the selected account, media platform, and workflow. Requires Node.js 18+ and siluzan-tso-cli.]

## Skill Version(s):

1.1.64 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
