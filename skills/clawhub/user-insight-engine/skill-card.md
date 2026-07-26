## Description: <br>
User Insight Engine helps agents diagnose gaps between what users say and what they do by synthesizing surface, behavioral, and deep-layer evidence into a driver and intervention. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product teams, user researchers, and agents use this skill to investigate behavior gaps such as high satisfaction with high churn, failed feature adoption, or conflicting research signals. It guides synthesis from surface statements, behavioral data, and deep-layer evidence into a primary driver and testable intervention. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide product or research decisions using user behavior data. <br>
Mitigation: Apply normal human review before acting on suggested drivers or interventions. <br>
Risk: Interventions can be unreliable when based on surface statements or behavioral data without deep-layer evidence. <br>
Mitigation: Use the skill's stop rule: require at least one deep-layer evidence item before proceeding to intervention guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deciqai/skills/user-insight-engine) <br>
- [User Insight Engine product page](https://www.deciqai.com/c/user-insight-engine) <br>
- [Machine-readable skill metadata](https://www.deciqai.com/s/user-insight-engine.json) <br>
- [Primary sources](references/sources.md) <br>
- [Taylor's Behavioral Observation at Bethlehem Steel](examples/taylors-behavioral-observation-at-bethlehem-steel-1898-1901.md) <br>
- [The Principles of Scientific Management](https://archive.org/details/principlesofscie00taylrich) <br>
- [Prospect Theory: An Analysis of Decision under Risk](https://www.jstor.org/stable/1914185) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown report card and step-by-step coaching prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May stop at WAIT checkpoints and requires behavioral plus deep-layer evidence before intervention guidance.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
