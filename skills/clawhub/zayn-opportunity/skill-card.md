## Description: <br>
Assesses whether a customer interaction is a routine inquiry, test purchase, active project, or long-term opportunity by reviewing current opportunity signals, missing conditions, and deal stage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, customer management, and business development users can use this skill to triage opportunity quality from a customer or project, the current demand, available evidence, and the assessment goal. It helps separate facts from assumptions, identify missing or conflicting signals, and decide whether to request more information before making a formal judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Opportunity assessments may involve sensitive customer, project, budget, or decision-maker details. <br>
Mitigation: Provide only information intended for analysis and avoid unnecessary sensitive data, consistent with the release security guidance. <br>
Risk: Incomplete, conflicting, or weak evidence could lead to overstated opportunity conclusions. <br>
Mitigation: Use the skill's parameter status checks, require at least one reliable evidence item, preserve conflicts for validation, and avoid treating assumptions as facts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-opportunity) <br>
- [Skill rules](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>
- [Usage template](artifact/examples.md) <br>
- [Test guidance](artifact/tests.md) <br>
- [Changelog](artifact/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance] <br>
**Output Format:** [Markdown with parameter status tables, opportunity classification, signal review, risks, current stage, and recommended next steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a customer or project, current demand, available evidence, and assessment goal before formal analysis; otherwise it asks for missing information or provides only a preliminary analysis.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact documents mention v0.1/0.1.0 draft status) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
