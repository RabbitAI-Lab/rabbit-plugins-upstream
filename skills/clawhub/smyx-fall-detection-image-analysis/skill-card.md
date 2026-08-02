## Description: <br>
Detects potential falls in a target area from images or short video clips and returns structured safety analysis for elder-care and facility monitoring scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, caregivers, facility operators, and developers use this skill to analyze uploaded images, short videos, or media URLs for possible falls and retrieve structured reports or cloud report history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Care-monitoring images, videos, or submitted URLs are sent to the lifeemergence.com/open.lifeemergence.com backend for analysis. <br>
Mitigation: Use the skill only with appropriate consent and privacy controls, and review retention, account-linkage, and deletion expectations before uploading sensitive in-home footage. <br>
Risk: The skill may create or reuse local identity state, authenticate with a backend, store tokens locally, and query cloud report history. <br>
Mitigation: Evaluate it in an isolated workspace and review or clear local identity and token state according to the deployment policy before and after use. <br>
Risk: Fall-detection results are safety guidance and may be incomplete or wrong. <br>
Mitigation: Treat results as advisory, verify suspected incidents with a human, and follow emergency response procedures when a possible fall is detected. <br>


## Reference(s): <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-fall-detection-image-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown/plain text with structured JSON report content and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local image/video files or public media URLs; report-list output is retrieved from the cloud API.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
