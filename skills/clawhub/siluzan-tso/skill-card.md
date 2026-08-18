## Description:

Siluzan TSO helps agents route advertising account management, campaign creation, reporting, market analysis, and operations workflows across Google, Bing, Yandex, TikTok, Kwai, and Meta Ads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing operators and agent developers use this skill to inspect ad accounts, manage campaign and account workflows, generate advertising reports, and prepare market or website diagnosis deliverables through Siluzan TSO tooling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents through workflows that change advertising accounts, budgets, permissions, or campaign state.

Mitigation: Require explicit human confirmation before write, destructive, budget, permission, or campaign publication actions.

Risk: The installer performs a global CLI and skill installation and changes npm registry configuration.

Mitigation: Review the installer before running it and install in a dedicated machine, shell profile, or account when handling business advertising access.

Risk: Generated reports and templates may include remote scripts or business-sensitive account data.

Mitigation: Review generated HTML before sharing, avoid pasting API keys or identity and financial documents into chat, and limit report distribution to authorized recipients.

## Reference(s):

- [Skill routing entrypoint](SKILL.md)
- [Reference index](references/README.md)
- [Intent routing](references/core/intent-routing.md)
- [Analysis and report playbooks](references/core/playbooks.md)
- [Operations workflows](references/core/workflows.md)
- [Google Ads reference](references/google-ads/google-ads.md)
- [Reporting reference](references/analytics/reporting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON payloads, report templates, and generated report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+ and siluzan-tso-cli authentication; workflows may produce HTML, Excel, or JSON artifacts depending on the task.]

## Skill Version(s):

1.1.45 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
