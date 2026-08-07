## Description: <br>
AI-powered cage cleanliness detection analyzes fixed-camera cage images or videos for feces and urine coverage, estimates cleanliness, and returns alerts or reports for boarding kennels, pet shops, animal hospitals, and breeding facilities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External operators and agents supporting pet boarding centers, pet shops, animal hospitals, and breeding facilities use this skill to analyze cage floor media, estimate waste coverage, produce cleanliness reports, and identify when cleaning attention is needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded cage media and report queries are processed by the Life Emergence cloud service. <br>
Mitigation: Use only media appropriate for that service and avoid unrelated or sensitive local files. <br>
Risk: The skill creates or reuses a local identity and stores service tokens in the workspace. <br>
Mitigation: Protect the workspace data, and review or delete the local database if access is revoked. <br>
Risk: Security evidence classifies the release as suspicious because it silently manages account identity, stores tokens locally, and uploads media to cloud services. <br>
Mitigation: Review the skill and its workspace storage behavior before deployment, especially in environments with privacy or data-retention requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-cage-cleanliness-detection-analysis) <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, API Calls, Files] <br>
**Output Format:** [Markdown report or JSON response, with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cleanliness scores, waste coverage estimates, alerts, report links, and historical report tables returned by the cloud service.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
