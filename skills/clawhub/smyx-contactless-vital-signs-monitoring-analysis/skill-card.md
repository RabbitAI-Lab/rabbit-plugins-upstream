## Description: <br>
Non-contact detection of heart rate, respiration, blood oxygen, and heart rate variability using camera footage without wearable devices. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze face video or image inputs for contactless vital-sign estimates and to retrieve prior monitoring reports. Results are informational health references and are not a substitute for professional medical measurement or diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Face/video health data and user-linked identifiers may be sent to the provider's cloud service. <br>
Mitigation: Use only with appropriate consent and review the provider's privacy, retention, and data-handling practices before submitting sensitive footage. <br>
Risk: The skill can create or reuse local identity state and store tokens for future report access. <br>
Mitigation: Run in an environment where local credential and identity state can be inspected, protected, and removed when access is no longer needed. <br>
Risk: Vital-sign analysis results may be mistaken for medical advice. <br>
Mitigation: Present results as informational health references only and direct users to professional medical measurement or diagnosis for health decisions. <br>


## Reference(s): <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-contactless-vital-signs-monitoring-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON health-analysis report with optional saved output file and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May retrieve cloud-hosted report history associated with internally managed user identity state.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release evidence; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
