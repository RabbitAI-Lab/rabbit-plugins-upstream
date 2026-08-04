## Description: <br>
Siluzan TSO routes agent work for advertising operations across Google, Bing, Yandex, TikTok, Kwai, and Meta, including account management, campaign creation, keyword planning, reporting, market analysis, website diagnosis, finance, and automation workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External advertising operations teams and agent users use this skill to route and execute Siluzan TSO ad-account, campaign, reporting, finance, and automation tasks through the Siluzan TSO CLI. It supports read-only analysis and report generation as well as higher-risk account, permission, finance, and ad-mutation workflows that require user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer and CLI require trust in a global command-line package and may modify global npm settings and multiple assistant skill directories. <br>
Mitigation: Install only after reviewing the publisher and CLI in an approved environment; document any global npm registry or assistant-directory changes. <br>
Risk: Authenticated use can access persistent credentials and broad advertising account, finance, and permission data. <br>
Mitigation: Use least-privileged accounts where possible, protect credentials, and revoke or rotate access when the skill is no longer needed. <br>
Risk: Ad publishing, deletion, permission, transfer, invoice, and account-opening workflows can mutate live business systems. <br>
Mitigation: Require explicit user confirmation before any write, publish, delete, permission, transfer, invoice, or account-opening action. <br>
Risk: Generated JSON exports and reports may contain sensitive business, financial, account, or personal data. <br>
Mitigation: Store exports and reports only in approved locations and avoid sharing them outside the authorized team. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sigedev01-bit/skills/siluzan-tso) <br>
- [Setup](references/core/setup.md) <br>
- [Intent routing](references/core/intent-routing.md) <br>
- [Playbooks](references/core/playbooks.md) <br>
- [Workflows](references/core/workflows.md) <br>
- [Reference index](references/README.md) <br>
- [Google Ads campaign plan](references/google-ads/google-ads-campaign-plan.md) <br>
- [Account balance and stats](references/accounts/accounts-balance-stats.md) <br>
- [Market analysis guide](references/analytics/market-analysis-guide.md) <br>
- [Website diagnosis guide](references/analytics/website-diagnosis-guide.md) <br>
- [Report templates](report-templates/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON templates, configuration instructions, and generated report files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 18+ and the siluzan-tso-cli; authenticated use may access credentials, ad accounts, finance data, and report exports.] <br>

## Skill Version(s): <br>
1.1.41 (source: server release evidence and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
