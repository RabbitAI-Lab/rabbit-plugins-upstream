## Description: <br>
A competitive SaaS, web, and app analysis workflow that uses browser automation to inspect competitor products and produce structured competitive-analysis reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[woai36d](https://clawhub.ai/user/woai36d) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product, design, strategy, and engineering teams can use this skill to inspect authorized competitor SaaS or web app accounts, capture page evidence, map menus and routes, compare features, and assemble structured competitive-analysis reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes plaintext third-party login credentials and guidance to reuse authenticated sessions. <br>
Mitigation: Install only with explicit authorization, remove plaintext credentials, rotate exposed passwords, avoid persistent cookie files, and use an interactive secure secret mechanism for login. <br>
Risk: Competitive analysis can collect information from third-party accounts without proper permission. <br>
Mitigation: Confirm authorization for each named account and collection target before running the workflow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/woai36d/skills/competitive-analysis) <br>
- [Case Summary](artifact/references/case-summary.md) <br>
- [Scoring Framework](artifact/references/scoring.md) <br>
- [Report Templates](artifact/references/templates.md) <br>
- [URL Routing Reference](artifact/references/url-routing.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Analysis, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports, URL inventories, scoring tables, screenshot files, and browser-automation command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses missing-data labels for unavailable or permission-limited findings and organizes deliverables by competitor and module.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
