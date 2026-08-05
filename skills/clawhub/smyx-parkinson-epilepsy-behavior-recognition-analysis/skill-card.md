## Description: <br>
Identifies abnormal behaviors such as limb tremors, convulsions, stiffness, and gait abnormalities through video recognition, assisting in home risk monitoring for patients with chronic conditions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and caregivers use this skill to analyze home monitoring images or videos for Parkinson's- and epilepsy-related abnormal movement indicators and to retrieve prior analysis reports. Results are for auxiliary monitoring and should not replace professional medical diagnosis or clinician judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive home-health images or videos may be uploaded to external lifeemergence.com services. <br>
Mitigation: Install and use only where users and recorded individuals have consented and the publisher's privacy, retention, and deletion practices are acceptable. <br>
Risk: Analysis and report history may be silently linked to external identity or account state. <br>
Mitigation: Review account-linking behavior before deployment and avoid use in environments where silent identity creation or reuse is not permitted. <br>
Risk: Service tokens may be stored in a workspace SQLite database. <br>
Mitigation: Restrict workspace access, review local storage handling, and remove local tokens when decommissioning the skill. <br>
Risk: Health-monitoring output may be mistaken for clinical diagnosis. <br>
Mitigation: Present results as auxiliary monitoring only and direct users to professional medical care for diagnosis or treatment decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-parkinson-epilepsy-behavior-recognition-analysis) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON text, with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured monitoring observations, risk notes, recommendations, report links, and cloud history tables; not a medical diagnosis.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
