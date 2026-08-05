## Description: <br>
Uses computer vision to detect and count coughing, phlegm, and wheezing in respiratory videos, producing health monitoring reports and early anomaly alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit respiratory symptom videos or URLs for cloud-based analysis, receive structured symptom counts, risk levels, suggestions, and report links, and query prior reports tied to the resolved user identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send health-related videos or URLs to Life Emergence cloud endpoints for processing. <br>
Mitigation: Use only when users understand and accept cloud processing of health media, and avoid submitting sensitive media unless that processing is appropriate for the use case. <br>
Risk: The skill can automatically create or reuse an identity, link history to that identity, and store authentication tokens in the workspace database. <br>
Mitigation: Run in a controlled workspace, review identity and token persistence before installation, and clear stored credentials or workspace state when the skill is no longer needed. <br>
Risk: The skill returns health monitoring outputs that may be mistaken for medical diagnosis. <br>
Mitigation: Treat outputs as advisory health-reference information and rely on qualified medical professionals for diagnosis, urgent symptoms, or treatment decisions. <br>


## Reference(s): <br>
- [Respiratory symptom recognition API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-respiratory-symptom-recognition-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown tables and structured JSON-style analysis reports with links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include health warnings, medical suggestions, report links, and historical report tables; results are health-reference outputs, not medical diagnoses.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release metadata; artifact frontmatter states 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
