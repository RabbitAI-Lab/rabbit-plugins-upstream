## Description:

Siluzan TSO helps agents route and execute ad account management, campaign planning, reporting, website diagnosis, market analysis, and lead-ad workflows across Google, Bing, Yandex, TikTok, and Meta Ads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Siluzan TSO advertising workflows, including account and finance tasks, search and PMax campaign planning, Meta Instant Form lead ads, optimization, reports, and market or website analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation and operation can grant persistent authority over advertising accounts and related finance workflows.

Mitigation: Install only for trusted Siluzan TSO use cases, prefer manual setup, and review any one-click installer changes before registration.

Risk: Write workflows can create campaigns, change budgets or bidding, alter account permissions, affect invoices, close accounts, change Lead Form behavior, or make irreversible PMax Brand Guidelines changes.

Mitigation: Require explicit human confirmation before any live write operation with financial, permission, account-state, lead-collection, or irreversible campaign effects.

Risk: The workflows may expose identity, bank, lead, or confidential business data in the agent conversation.

Mitigation: Use approved secure channels and retention controls before sharing sensitive account, finance, lead, or confidential business data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sigedev01-bit/skills/siluzan-tso)
- [Siluzan TSO Documentation Index](artifact/AGENTS.md)
- [Setup and Authentication Requirements](artifact/references/core/setup.md)
- [Account Management Workflows](artifact/references/accounts/accounts-list.md)
- [Google Ads Workflows](artifact/references/google-ads/google-ads.md)
- [Meta Ads Workflows](artifact/references/meta-ads/meta-ads.md)
- [Reporting Workflow](artifact/report-templates/REPORT-WORKFLOW.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, HTML, XLSX, and shell-command guidance depending on the selected workflow]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some workflows invoke the siluzan-tso CLI and may create local report or campaign-plan files.]

## Skill Version(s):

1.1.48 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
