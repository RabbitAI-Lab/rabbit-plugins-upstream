## Description: <br>
Clause-by-clause BAA analysis against 45 CFR 164.504(e)(2), evaluating all 9 required HIPAA provisions with risk scoring and remediation recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dangsllc](https://clawhub.ai/user/dangsllc) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Compliance teams, legal reviewers, and developers use this skill to review Business Associate Agreements against HIPAA BAA requirements and produce clause-level findings, risk ratings, and remediation recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded or pasted BAAs may contain PHI, patient identifiers, or confidential business details. <br>
Mitigation: Use the skill only in environments approved for that data and redact unnecessary PHI, patient identifiers, and irrelevant confidential details when possible. <br>
Risk: Compliance findings and remediation language may be incomplete or unsuitable for a specific organization or jurisdiction. <br>
Mitigation: Have qualified HIPAA or legal reviewers validate findings before relying on the report for contracting, audit, or compliance decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dangsllc/skills/baa-review) <br>
- [Rote Compliance](https://rotecompliance.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, guidance] <br>
**Output Format:** [JSON structured compliance report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes party identification, provision-level findings, BAA excerpts, risk levels, reasoning, and remediation recommendations.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata; SKILL.md frontmatter: 1.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
