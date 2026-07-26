## Description: <br>
PRD review stress-test simulator where five cross-functional roles challenge product requirements and produce a scored HTML or Markdown survival report with a radar chart and meeting script. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chris1wang3](https://clawhub.ai/user/chris1wang3) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product managers and product teams use this skill before requirements review meetings to rehearse cross-functional objections, score PRD readiness, prepare responses, assign RACI ownership, and generate meeting assets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger phrases for challenging or stress-testing a plan could activate the PRD review simulator when the user intended a different type of critique. <br>
Mitigation: For ambiguous requests, confirm that the user wants the PRD review simulator before proceeding. <br>
Risk: Simulated Go, Conditional Go, or No Go recommendations may be mistaken for final product, legal, or business approval. <br>
Mitigation: Keep the report advisory, include the skill's disclaimer, and require qualified human review for final decisions, especially in regulated domains. <br>
Risk: Sparse or ambiguous PRD inputs can produce conservative scores and incomplete review coverage. <br>
Mitigation: Use the intake form or checklist, mark inferred and missing information clearly, and ask for confirmation before generating the final HTML or Markdown report. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chris1wang3/skills/pm-requirement-review-simulator) <br>
- [Intake form](assets/intake-form.html) <br>
- [Review Defense Playbook](references/review-playbook.md) <br>
- [Deterministic Scoring Engine](references/scoring-engine-deterministic.md) <br>
- [HTML Report Template](references/report-template-pro.html) <br>
- [User Templates](references/user_templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [HTML or Markdown report with structured scoring details, role challenges, RACI assignments, meeting script, action checklist, and disclaimer.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can use a reusable HTML intake form before report generation; output format is selected by the user.] <br>

## Skill Version(s): <br>
1.2.8 (source: artifact/claw.json and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
