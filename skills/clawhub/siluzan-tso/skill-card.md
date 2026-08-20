## Description:

Siluzan TSO routes advertising account management, campaign operations, reporting, diagnostics, keyword planning, market analysis, and hosted automation workflows for Google, Bing, Yandex, TikTok, Kwai, and Meta Ads through the siluzan-tso CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit)

### License/Terms of Use:

MIT-0

## Use Case:

External advertising operators and developers use this skill to select the correct TSO workflow, run siluzan-tso CLI commands, manage advertising accounts and campaigns, and produce diagnostics, period reports, website checks, keyword plans, and market analysis deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation and setup can make persistent local changes through CLI installation and assistant registration.

Mitigation: Review the installer before running it, install only from trusted release material, and use an isolated environment when evaluating the skill.

Risk: The workflows can handle advertising accounts, budgets, financial operations, API keys, account-opening data, lead data, and other sensitive business information.

Mitigation: Use least-privilege credentials, keep secrets and raw personal or billing data out of shared logs and repositories, and restrict access to users who are trusted with the underlying accounts.

Risk: Write, budget, financial, or permission workflows can affect live advertising spend or account state.

Mitigation: Require explicit human confirmation for every write or financial action and use the artifact's audit and restore guidance when reviewing or recovering changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sigedev01-bit/skills/siluzan-tso)
- [Skill routing entrypoint](SKILL.md)
- [Intent routing](references/core/intent-routing.md)
- [Playbooks](references/core/playbooks.md)
- [Workflows](references/core/workflows.md)
- [Setup](references/core/setup.md)
- [Account analytics](references/analytics/account-analytics.md)
- [Market analysis guide](references/analytics/market-analysis-guide.md)
- [Website diagnosis guide](references/analytics/website-diagnosis-guide.md)
- [Google Ads workflows](references/google-ads/google-ads.md)
- [Hosted automation catalog](references/operations/hosted-automation-user-catalog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON templates, HTML or Excel report deliverables, and generated configuration files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+, siluzan-tso-cli, and authenticated Siluzan TSO credentials; write, financial, and account-permission actions require explicit confirmation.]

## Skill Version(s):

1.1.46 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
