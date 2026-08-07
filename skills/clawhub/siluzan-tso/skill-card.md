## Description:

Siluzan TSO routes agents through Siluzan advertising workflows for account management, Google, Bing, Yandex, TikTok, Kwai, and Meta ad operations, reporting, market analysis, keyword planning, alerts, finance, and hosted automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit)

### License/Terms of Use:

MIT-0

## Use Case:

External teams and operators use this skill to guide an agent through Siluzan TSO ad-account operations, campaign creation, reporting, diagnostics, optimization, finance, alerts, and market-analysis workflows. It is intended for authenticated Siluzan CLI use where live advertising accounts and business data may be involved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a global, persistent advertising-operations CLI installation.

Mitigation: Install only after reviewing the installer and trusting the Siluzan CLI publisher; prefer manual installation through the normal npm registry on a non-shared machine.

Risk: The workflows can affect live ad accounts, budgets, deletions, withdrawals, lead exports, and account-opening actions.

Mitigation: Require explicit human confirmation before any live account, budget, deletion, withdrawal, lead export, or account-opening operation.

Risk: Generated reports, account snapshots, and raw lead outputs may contain sensitive business or personal data.

Mitigation: Restrict where outputs are stored and shared, and handle exported reports and lead data as sensitive material.

Risk: Authentication uses persistent Siluzan credentials or environment-provided tokens.

Mitigation: Use short-lived or scoped credentials when available, avoid shared machines, and clear or rotate credentials after use in temporary environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sigedev01-bit/skills/siluzan-tso)
- [Skill Definition](SKILL.md)
- [Reference Index](references/README.md)
- [Setup and Authentication](references/core/setup.md)
- [Intent Routing](references/core/intent-routing.md)
- [Analysis Playbooks](references/core/playbooks.md)
- [Operations Workflows](references/core/workflows.md)
- [Google Ads Campaign Planning](references/google-ads/google-ads-campaign-plan.md)
- [Account Analytics](references/analytics/account-analytics.md)
- [Guard Automation](references/operations/guard.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands, JSON snapshots, HTML or Excel report files, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+, siluzan-tso-cli, and authenticated Siluzan credentials.]

## Skill Version(s):

1.1.43 (source: server release evidence and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
