## Description: <br>
Generates an industry-specific ROI estimate card from customer industry, company size, scenario, and current cost inputs for presales value discussions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[william202404](https://clawhub.ai/user/william202404) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, product, and technical presales teams use this skill to quantify an AI value proposition, shape PoC scope, and prepare customer-facing ROI discussion material. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ROI estimates may be mistaken for audited financial advice or committed business outcomes. <br>
Mitigation: Use the output as sales-planning guidance only and confirm assumptions, costs, and financial conclusions with the appropriate pricing or finance owners before customer commitments. <br>
Risk: Sensitive customer details may be entered as command-line arguments. <br>
Mitigation: Avoid confidential customer information unless local tooling policy permits that data in command-line arguments; use sanitized inputs for examples and drafts. <br>
Risk: Incomplete inputs or unusually high ROI results can produce misleading estimates. <br>
Mitigation: Review the reported confidence level, deviation range, and anomaly warnings, and gather missing cost or headcount data before using the card for PoC gates or executive review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/william202404/skills/industry-roi-calculator) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown report with ROI estimates, PoC scope, risk assumptions, de-identified case references, and next steps.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses command-line inputs such as industry, company size, scenario, current cost, headcount, average salary, deployment level, pain points, target metric, and deal size.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact frontmatter/package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
