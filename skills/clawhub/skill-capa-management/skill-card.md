## Description: <br>
A Chinese-language CAPA corrective-action consultant that tailors audit-ready and practical remediation plans by organization maturity, enforces a three-question maturity assessment, and produces six-section txt and markdown reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality managers, auditors, and operations teams use this skill to structure corrective and preventive action responses for customer complaints, audit nonconformities, and process issues. It guides users through maturity assessment, fact capture, containment, root-cause analysis, corrective actions, verification, and standardization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated CAPA reports may contain incomplete or incorrect corrective-action guidance if the user's facts, root cause, or evidence are incomplete. <br>
Mitigation: Have the responsible quality owner review the facts, root-cause analysis, corrective actions, standard references, and supporting evidence before audit or customer submission. <br>
Risk: The skill may generate report files in a user-selected output directory. <br>
Mitigation: Confirm the intended output directory before running report generation. <br>
Risk: The inspected artifact references helper resources that were not included. <br>
Mitigation: Verify that required helper resources and scripts are available before relying on automated report generation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/duding-engicool/skills/skill-capa-management) <br>
- [Server-resolved GitHub provenance](https://github.com/duding-engicool/skill-capa-management) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands] <br>
**Output Format:** [Markdown and plain text report files, with concise procedural guidance and optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended for internal or formal audit documentation and depend on user-provided facts, evidence, and maturity-assessment answers.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
