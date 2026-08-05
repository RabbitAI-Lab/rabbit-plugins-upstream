## Description: <br>
This skill analyzes turtle enclosure video inputs to identify visual respiratory warning signs such as frequent open-mouth breathing, mouth or nasal mucus, nasal discharge, abnormal posture, and related pneumonia-risk alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, reptile keepers, breeders, animal-care staff, and developers can use this skill to submit turtle enclosure footage for visual respiratory-sign analysis and to review generated pneumonia-risk warning reports. It supports analysis of current footage and retrieval of cloud-hosted historical warning reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends turtle videos or URLs to the lifeemergence.com cloud service for processing. <br>
Mitigation: Use it only with footage that may be processed by that cloud service, and avoid sensitive footage unless local policies allow that processing. <br>
Risk: The skill silently creates or reuses a local identity, registers or logs into the remote service, and stores returned tokens in the workspace data database. <br>
Mitigation: Review workspace access, local data retention, and token deletion practices before use in shared or sensitive environments. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-turtle-pneumonia-symptom-detection-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [Skill Usage Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON or Markdown text report with report links and optional file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include visual analysis results, warning levels, recommended next actions, disclaimers, and report export links when returned by the service.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
