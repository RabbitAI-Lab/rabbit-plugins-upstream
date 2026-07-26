## Description: <br>
Assess compliance documents against HIPAA Security Rule and Privacy Rule requirements, producing structured findings with evidence, gap descriptions, and remediation recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dangsllc](https://clawhub.ai/user/dangsllc) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Compliance, security, and healthcare operations teams use this skill to review user-provided policy or procedure documents against HIPAA Security Rule and Privacy Rule requirements. It identifies covered, partial, and missing control coverage with direct evidence and remediation recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided compliance documents may contain sensitive policy or healthcare-related information. <br>
Mitigation: Review documents before attaching or directing the agent to read them, and handle generated findings according to the same confidentiality requirements as the source material. <br>
Risk: Gap-analysis findings may be mistaken for legal or regulatory advice. <br>
Mitigation: Use the output as compliance support and have qualified privacy, security, or legal reviewers validate conclusions before relying on them for audit or remediation decisions. <br>
Risk: Quoted evidence in findings can reproduce sensitive source-document content. <br>
Mitigation: Limit distribution of the generated JSON and redact quoted evidence when sharing outside the intended review team. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dangsllc/skills/hipaa-gap-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/dangsllc) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, guidance] <br>
**Output Format:** [Structured JSON findings with concise explanatory text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Findings include document title, analysis date, framework summary, per-control status, direct evidence, gap descriptions, recommendations, confidence, and reasoning.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
