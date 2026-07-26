## Description: <br>
Guides an agent through SWOT and TOWS strategic analysis to produce a bounded strategic audit with strengths, weaknesses, opportunities, threats, strategy options, priorities, and review triggers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external consultants, and strategy teams use this skill to structure business planning, market-entry review, investor-prep analysis, crisis mapping, or competitive audits into an evidence-backed SWOT and TOWS strategic audit. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate for broad strategic planning, market-entry, or investor-prep requests where the user did not explicitly ask for SWOT. <br>
Mitigation: Confirm the decision context and bounded analysis unit before producing the audit, and redirect to a better-fit strategy tool when the request needs financial modeling, industry-structure mapping, or growth-direction selection. <br>
Risk: Strategic recommendations can be misleading if subjective SWOT entries are treated as evidence or if internal strengths are confused with external opportunities. <br>
Mitigation: Require named competitors, measurable comparative strengths, external opportunities, probability and impact ratings for threats, TOWS cross-pairs, and explicit deprioritization before presenting top strategies. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deciqai/skills/swot-analysis) <br>
- [Primary sources](references/sources.md) <br>
- [SWOT Analysis for Management Consulting](https://www.sri.com/hoi/sriaa.html) <br>
- [The TOWS Matrix - A Tool for Situational Analysis](https://doi.org/10.1016/0024-6301(82)90120-0) <br>
- [Netflix annual reports](https://ir.netflix.net/ir/doc/annual-reports) <br>
- [Skill machine-readable metadata](https://www.deciqai.com/s/swot-analysis.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown strategic audit with SWOT quadrants, TOWS cross-matrix, prioritized actions, deprioritized options, and verification checklist] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May run interactively in coach mode, pausing for user input before advancing through the audit.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
