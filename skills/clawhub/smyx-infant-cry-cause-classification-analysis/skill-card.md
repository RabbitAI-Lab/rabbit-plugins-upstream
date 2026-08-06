## Description: <br>
This skill analyzes infant cry audio or audio-bearing video through a cloud service and returns likely cry causes, confidence, supporting acoustic features, calming suggestions, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, nursery operators, daycare staff, and developers use this skill to classify likely causes of infant crying from uploaded audio, video, or URLs and to retrieve cloud-hosted historical reports. Results are parenting support signals and should not be treated as medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Infant or household recordings and historical reports are processed through a cloud service and linked to persistent identities. <br>
Mitigation: Verify guardian consent before use, disclose cloud processing, and confirm users have an appropriate way to manage or delete stored reports and tokens. <br>
Risk: Cry-cause classifications may be mistaken for clinical guidance. <br>
Mitigation: Present results as non-diagnostic parenting support and direct caregivers to seek professional care for persistent, severe, or medically concerning crying. <br>
Risk: History queries can expose sensitive prior infant cry reports. <br>
Mitigation: Limit report access to the intended account context and review outputs before sharing report links or exported report images. <br>


## Reference(s): <br>
- [Infant Cry Cause Classification API Documentation](references/api_doc.md) <br>
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Files, Shell commands] <br>
**Output Format:** [Markdown text containing structured JSON-style analysis, report links, and optional saved result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May upload local media or submit media URLs to the configured cloud service; history listing is returned from the cloud API.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter says 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
