## Description:

Siluzan TSO helps agents operate and analyze Siluzan advertising workflows across Google, Bing, Yandex, TikTok, Kwai, and Meta, including account management, campaign planning, reporting, website diagnosis, keyword planning, and market analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ad-operations teams use this skill to route Siluzan TSO requests, run the required CLI workflows, create or inspect ad campaigns, manage accounts and finance tasks, and produce advertising, website, keyword, and market-analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can handle live advertising accounts, finance workflows, credentials, and personal or lead data.

Mitigation: Use only accounts the operator is authorized to manage, avoid pasting full IDs, bank numbers, API keys, or raw lead records into chat logs, and keep sensitive data in local files where possible.

Risk: Installer and setup flows can persist credentials and register the skill or CLI across multiple AI clients.

Mitigation: Review the installer before use and prefer a manual install that only targets the AI client and workspace intended for this deployment.

Risk: The skill includes workflows that can write, pause, delete, close, withdraw, change permissions, or alter ad budgets.

Mitigation: Require explicit human confirmation before any write, destructive, permission, financial, or budget action, and verify the result with the documented read-back command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sigedev01-bit/skills/siluzan-tso)
- [ClawHub publisher profile](https://clawhub.ai/user/sigedev01-bit)
- [Reference index](artifact/references/README.md)
- [Setup and authentication](artifact/references/core/setup.md)
- [Operational workflows](artifact/references/core/workflows.md)
- [Analysis and reporting playbooks](artifact/references/core/playbooks.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown, Files]

**Output Format:** [Markdown guidance with CLI commands, JSON configuration, HTML or Excel report files, and structured handoff text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+, the siluzan-tso-cli package, and authenticated Siluzan credentials for live account operations.]

## Skill Version(s):

1.1.44 (source: server release metadata and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
