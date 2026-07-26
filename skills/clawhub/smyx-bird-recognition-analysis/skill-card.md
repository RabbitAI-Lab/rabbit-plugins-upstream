## Description: <br>
Identifies bird species in images or videos, supports recognition of at least 500 common species, and can produce structured bird-recognition reports for ecological observation and birdwatching use cases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze bird images, videos, or URLs, identify likely species, and retrieve prior cloud-generated recognition reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends bird images, videos, URLs, and an internal user identifier to a remote Life Emergence service for processing. <br>
Mitigation: Install and use it only when remote processing of those inputs is acceptable for the user, organization, and data involved. <br>
Risk: The skill can create local workspace data that may include reusable account or session tokens. <br>
Mitigation: Prefer a release that documents storage and cleanup behavior, and review local workspace data handling before deployment. <br>
Risk: The skill supports cloud history access for account-linked recognition reports. <br>
Mitigation: Confirm that cloud history access is expected and appropriately disclosed before using report-listing features. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-bird-recognition-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands] <br>
**Output Format:** [Markdown or JSON text with report links and recognition results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report links and historical report listings.] <br>

## Skill Version(s): <br>
1.0.14 (source: server release metadata; SKILL.md frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
