## Description:

Helps advertising teams manage accounts and campaigns, analyze performance, and produce reports across Google, Meta, TikTok, Bing, and Yandex through Siluzan TSO.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit)

### License/Terms of Use:

MIT-0

## Use Case:

Advertising teams and their agents use this skill to inspect ad accounts, plan and manage supported campaigns, monitor spending, and prepare performance, website, and market-analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation can add a global command-line tool and store credentials persistently.

Mitigation: Install only if you trust the publisher; prefer a scoped, manually reviewed installation over the one-click global installer.

Risk: Ad account operations can make consequential changes to campaigns, budgets, or access.

Mitigation: Review proposed changes and grant only the access needed; explicitly confirm account changes before execution.

Risk: Admin-level account invitations can grant broad control.

Mitigation: Review the recipient and requested permission level before sending an invitation.

Risk: Raw lead records may expose contact details in a conversation.

Mitigation: Avoid requesting or sharing raw lead JSON unless every recipient is authorized to see the contact details.

## Reference(s):

- [Siluzan TSO release](https://clawhub.ai/sigedev01-bit/skills/siluzan-tso)
- [Setup and authentication](artifact/references/core/setup.md)
- [Workflow routing](artifact/references/core/intent-routing.md)
- [Account permissions](artifact/references/accounts/accounts-permissions.md)
- [Reporting workflows](artifact/references/report-templates/REPORT-WORKFLOW.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Reports]

**Output Format:** [Text and Markdown guidance; JSON, HTML, and spreadsheet report files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account changes require explicit user confirmation.]

## Skill Version(s):

1.1.55 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
