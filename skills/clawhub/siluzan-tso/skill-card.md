## Description: <br>
Siluzan TSO helps agents route and execute advertising account, campaign, reporting, market analysis, and operations workflows for the TSO ad platform through the siluzan-tso CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Advertising operations teams, developers, and agents use this skill to select the correct TSO workflow for ad account management, campaign creation, reporting, diagnostics, keyword planning, market analysis, finance, permissions, and operational monitoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can affect campaigns, accounts, reports, permissions, invoices, and local assistant configuration. <br>
Mitigation: Install and use it only for trusted TSO accounts, keep access scoped to the needed task, and require review before write actions or permission and finance operations. <br>
Risk: The one-click installers perform broad local setup, including global CLI installation and assistant skill registration. <br>
Mitigation: Prefer manual or scoped installation after reading the installer scripts, and avoid one-click installation on sensitive workstations. <br>
Risk: Workflows may handle sensitive URLs, market plans, account data, PII, financial records, and generated HTML reports that load remote scripts. <br>
Mitigation: Limit inputs to necessary data, review generated reports before sharing, and avoid opening generated HTML in high-trust browser sessions when remote script loading is a concern. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sigedev01-bit/skills/siluzan-tso) <br>
- [Publisher profile](https://clawhub.ai/user/sigedev01-bit) <br>
- [References index](references/README.md) <br>
- [Setup guide](references/core/setup.md) <br>
- [Intent routing](references/core/intent-routing.md) <br>
- [Core playbooks](references/core/playbooks.md) <br>
- [Core workflows](references/core/workflows.md) <br>
- [Account analytics](references/analytics/account-analytics.md) <br>
- [Google Ads campaign planning](references/google-ads/google-ads-campaign-plan.md) <br>
- [Market analysis guide](references/analytics/market-analysis-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON payloads, and generated report files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce HTML, Excel, JSON, or campaign configuration files depending on the selected TSO workflow.] <br>

## Skill Version(s): <br>
1.1.38 (source: server release metadata and _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
