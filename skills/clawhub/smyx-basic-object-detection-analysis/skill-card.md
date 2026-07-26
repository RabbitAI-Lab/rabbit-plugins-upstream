## Description: <br>
Detects people, vehicles, non-motorized vehicles, pets, and parcels in images or video streams for general security surveillance scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Security operators and developers use this skill to run basic object detection on surveillance images, videos, or URLs and produce structured detection reports, recommendations, and report links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Surveillance images, videos, or URLs may be sent to configured lifeemergence.com cloud services. <br>
Mitigation: Use only when the publisher's cloud processing, retention, and account controls are acceptable; avoid sensitive footage when those controls are not confirmed. <br>
Risk: The skill can silently create or reuse an identity and store service tokens locally. <br>
Mitigation: Review identity handling and token storage before deployment, and use a separate workspace for installations. <br>
Risk: Keyword-triggered history retrieval can access cloud-stored analysis reports. <br>
Mitigation: Limit use to authorized accounts and review report-history access controls before enabling the skill. <br>


## Reference(s): <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-basic-object-detection-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands] <br>
**Output Format:** [Markdown reports and structured JSON from command-line execution] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save report text to a user-specified output file; supports local media paths and public media URLs.] <br>

## Skill Version(s): <br>
1.0.9 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
