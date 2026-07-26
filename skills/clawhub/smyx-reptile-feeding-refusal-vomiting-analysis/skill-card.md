## Description: <br>
Through fixed enclosure cameras, the skill analyzes reptile feeding-time and post-feeding videos to detect prey attack behavior, successful swallowing, feeding refusal, and regurgitation or vomiting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, reptile keepers, vivarium operators, and developers use this skill to analyze enclosure camera media for feeding refusal, swallowing, and vomiting events, then produce structured event reports and care-oriented alerts. The output is behavioral monitoring support, not veterinary diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reptile videos, video URLs, and account-linked identifiers may be sent to the publisher's cloud service. <br>
Mitigation: Use only media approved for cloud processing and review the publisher's retention, access, and sharing practices before deployment. <br>
Risk: The skill may silently create or reuse an internal identity and store local identity tokens. <br>
Mitigation: Run it in an isolated environment, review local token storage, and require explicit operational approval before enabling it for shared users. <br>
Risk: Cloud report history queries can expose account-linked historical feeding events. <br>
Mitigation: Limit history access to authorized users and verify that report links and event lists are appropriate for the deployment context. <br>
Risk: Behavioral detections and care suggestions could be mistaken for veterinary diagnosis. <br>
Mitigation: Present outputs as visual monitoring records and route urgent vomiting or repeated abnormal refusal events to a qualified reptile veterinarian. <br>


## Reference(s): <br>
- [API Interface Documentation](artifact/references/api_doc.md) <br>
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON report text with event classifications, confidence values, recommendations, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May query cloud-hosted history and may write an optional local output file when requested.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
