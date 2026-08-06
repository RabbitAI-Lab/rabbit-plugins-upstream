## Description: <br>
Accounting Finance helps financial analysts, institutional investors, and corporate finance teams run valuation modeling, financial analysis, risk assessment, batch processing, and automated report generation workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Financial analysts, institutional investors, and corporate finance teams use this skill to automate valuation modeling, financial statement analysis, fraud and risk checks, batch monitoring, and report generation. Developers can configure Python-based workflows and optional market-data providers for repeatable finance analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Finance workspaces may contain unpublished or confidential financial data, and the skill can read and write finance files and generated reports. <br>
Mitigation: Run the skill in a protected workspace, restrict access to generated reports, and avoid using confidential financial data unless the workspace and workflow are approved for that data. <br>
Risk: Optional market-data providers require API keys and may send financial queries to external services. <br>
Mitigation: Store API keys securely, configure only the providers intended for the workflow, and avoid external provider calls when unpublished or confidential data should remain local. <br>
Risk: Generated valuation and risk outputs depend on input quality, assumptions, and configured models. <br>
Mitigation: Have qualified finance reviewers validate source data, model assumptions, and generated reports before using outputs for business, investment, or compliance decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/accounting-finance) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON, YAML, and Python examples plus generated report artifacts when configured] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and write local finance files, run Python analysis, and generate PDF, DOCX, HTML, or Excel reports when configured.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
