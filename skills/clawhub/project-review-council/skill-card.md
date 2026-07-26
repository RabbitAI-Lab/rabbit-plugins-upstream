## Description: <br>
Project Review Council runs a structured, evidence-first project review council for audits, retrospectives, risk analysis, and Go/No-Go decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qomob](https://clawhub.ai/user/qomob) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, founders, product teams, and reviewers use this skill to assess projects across strategy, technology, product, security, growth, finance, competition, and execution. It guides a phased review that produces role reports, risk rankings, business and execution evaluations, and a final decision memo. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Adversarial, competitor, or Red Team review prompts could be framed as instructions to target real third parties or systems. <br>
Mitigation: Frame those sections as defensive scenario analysis, abuse-case review, and mitigation planning, consistent with the ClawScan guidance. <br>
Risk: Project decisions may be over-weighted if evidence is incomplete or role reports converge without independent reasoning. <br>
Mitigation: Use the skill's strict evidence tags, user checkpoints, cross-review phase, and independent auditor phase before relying on the final decision memo. <br>


## Reference(s): <br>
- [Project Review Council GitHub repository](https://github.com/qomob/project-review-council) <br>
- [Project Review Council on ClawHub](https://clawhub.ai/qomob/skills/project-review-council) <br>
- [Decision matrix rubric](artifact/rubrics/decision-matrix.md) <br>
- [Final decision memo template](artifact/templates/decision-memo.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown reports, scorecards, risk tables, and decision memos] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Evidence tags are expected for conclusions; default configuration uses Chinese output, strict evidence marking, and phased review checkpoints.] <br>

## Skill Version(s): <br>
0.1.1 (source: target metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
