## Description: <br>
Based on computer vision, this skill detects and recognizes cats and dogs from smart feeder or IPC camera media, supports pet identity recognition and enrollment, and returns structured pet recognition reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze smart feeder or IPC camera images, videos, or media URLs for cat and dog detection, pet identity recognition, pet enrollment, and cloud report history lookup. The results support smart feeding workflows and should be treated as advisory rather than a substitute for human confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Private pet-camera images, videos, media URLs, and identity-linked report history may be processed by the Life Emergence cloud service. <br>
Mitigation: Use only media appropriate for that service, avoid private or internal URLs and token-bearing links, and obtain user consent before analysis or history lookup. <br>
Risk: The skill may retain locally resolved account tokens or default identity data in the workspace. <br>
Mitigation: Review or delete the workspace data database and stored API key file when local token retention is not desired. <br>
Risk: Pet detection and identity recognition results may be incorrect or incomplete for feeding decisions. <br>
Mitigation: Treat results as smart-feeding guidance and confirm important outcomes manually before acting on them. <br>


## Reference(s): <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-detection-feeder-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown reports and JSON structured results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include detection results, enrollment results, report-history tables, suggestions, report links, and optional file output.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
