## Description: <br>
Generates structured test analysis reports from Pytest, Allure, Jest, JUnit, logs, or manual test data, with metrics, failure analysis, trends, dashboards, and exports to Markdown, HTML, PDF, or Excel. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shylamb-token](https://clawhub.ai/user/shylamb-token) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, and release teams use this skill to turn test execution outputs and logs into readable quality reports, failure analysis, trend summaries, and exportable dashboards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: HTML reports may load Chart.js from a remote CDN when opened. <br>
Mitigation: Review generated HTML before sharing or opening in restricted environments, and replace the CDN dependency with an approved local asset when remote loading is not acceptable. <br>
Risk: Generated reports can expose sensitive details from test logs, including failure messages and environment information. <br>
Mitigation: Avoid including sensitive logs in shared reports, redact confidential values before export, and choose output paths deliberately. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shylamb-token/skills/smart-test-report) <br>
- [Publisher profile](https://clawhub.ai/user/shylamb-token) <br>
- [Chart.js CDN used by HTML report template](https://cdn.jsdelivr.net/npm/chart.js) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown reports, generated code snippets, and export guidance for HTML, PDF, Excel, and Markdown outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include parsed metrics, failure classifications, trend summaries, charts, and remediation recommendations derived from user-provided test data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
