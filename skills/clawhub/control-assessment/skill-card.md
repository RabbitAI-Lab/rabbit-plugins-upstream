## Description: <br>
Evaluate individual framework controls against organizational documentation with evidence extraction, severity classification, and remediation recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dangsllc](https://clawhub.ai/user/dangsllc) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Compliance, security, and audit teams use this skill to assess one framework control at a time against organizational documentation, quote supporting evidence, classify coverage gaps, and produce remediation recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Organizational compliance documents may contain sensitive policy, security, or regulatory information. <br>
Mitigation: Use the skill only with documents the agent is intended to review, and check outputs before sharing them externally. <br>
Risk: Control coverage, severity, or remediation recommendations may be incomplete when the supplied document set or control context is incomplete. <br>
Mitigation: Review quoted evidence, gap descriptions, and severity classifications with an appropriate compliance or security reviewer before relying on the assessment for audit or remediation decisions. <br>


## Reference(s): <br>
- [Control Assessment on ClawHub](https://clawhub.ai/dangsllc/skills/control-assessment) <br>
- [dangsllc Publisher Profile](https://clawhub.ai/user/dangsllc) <br>
- [Rote Compliance Skills](https://github.com/Rote-Compliance/rote-compliance-skills) <br>
- [Rote](https://rotecompliance.com) <br>
- [Dang's Solutions](https://dangssolutions.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown containing structured JSON assessment objects] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Each control assessment includes control metadata, coverage status, quoted evidence, gap description, severity, recommendations, confidence, and reasoning.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
