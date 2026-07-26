## Description: <br>
Analyzes respiratory symptom videos or URLs with a cloud vision API to detect coughing, phlegm, and wheezing frequency, then returns structured health-monitoring results and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and health-monitoring agents use this skill to analyze respiratory symptom videos or URLs, retrieve cloud-generated monitoring reports, and view historical report records. Results are for health reference and early anomaly awareness, not medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive respiratory or health-related videos or URLs are sent to the publisher's cloud service. <br>
Mitigation: Obtain explicit user confirmation before uploads and avoid patient-identifying media unless the workspace and service terms are appropriate. <br>
Risk: The skill creates or reuses a local identity and stored API tokens for report history. <br>
Mitigation: Use isolated workspaces for shared environments and review identity and token handling before enabling history queries. <br>
Risk: Health-monitoring analysis may be misleading if treated as diagnosis. <br>
Mitigation: Present results as reference information only and direct users to medical professionals for diagnosis or urgent respiratory symptoms. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-respiratory-symptom-recognition-analysis) <br>
- [Respiratory symptom recognition API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands] <br>
**Output Format:** [Markdown text with structured JSON analysis results and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save analysis output to a local file when an output path is provided.] <br>

## Skill Version(s): <br>
1.0.10 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
