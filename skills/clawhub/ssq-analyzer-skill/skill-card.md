## Description: <br>
SSQ (Double Color Ball) lottery analysis skill that fetches official draw data, computes historical statistics and trend reports, and provides paid number recommendations after third-party verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Users who want Chinese-language SSQ lottery analysis can use this skill to update official draw data, review hot/cold number statistics, inspect distribution trends, and optionally request paid recommendation sets after clawtip verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lottery recommendations may be mistaken for guaranteed outcomes even though lottery draws are random independent events. <br>
Mitigation: Present recommendations as statistical analysis only, include responsible-purchase warnings, and avoid claims of guaranteed winnings. <br>
Risk: The skill contacts cwl.gov.cn for draw data and api.ideaidea.com.cn for order and payment verification while reading a local clawtip payment credential. <br>
Mitigation: Install only when these network and credential behaviors are acceptable, avoid sensitive personal details in question text, and review local order files before use. <br>
Risk: Security evidence notes that paid recommendation gating appears weak and delivery behavior should be treated cautiously. <br>
Mitigation: Verify order and payment status before relying on paid recommendation delivery, and treat paid results as advisory until the flow is reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinyu12166/skills/ssq-analyzer-skill) <br>
- [Publisher profile](https://clawhub.ai/user/jinyu12166) <br>
- [China Welfare Lottery draw data source](https://www.cwl.gov.cn) <br>
- [clawtip verification service endpoint](https://api.ideaidea.com.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Chinese-language text and Markdown reports with inline shell commands and local data files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local SQLite draw data, order metadata, and a Markdown analysis report; paid recommendations require third-party clawtip verification.] <br>

## Skill Version(s): <br>
1.0.23 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
