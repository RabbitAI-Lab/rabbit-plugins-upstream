## Description: <br>
Analyzes full-plant images or videos to quantify wilting severity, identify likely underwatering or overwatering signals, and produce structured irrigation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze plant media from smart pots, fixed cameras, home gardens, greenhouses, or plant factories and receive a wilting score, likely cause, and intervention direction. It is intended to support plant-care decisions, not to prescribe exact watering quantities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant images, videos, and supplied URLs are sent to lifeemergence.com services for analysis. <br>
Mitigation: Use only media and URLs that are acceptable to share with that service, and avoid private images or internal network URLs unless the publisher's data handling is approved. <br>
Risk: Cloud report history is associated with an internal identifier. <br>
Mitigation: Confirm the intended identity context before use and review the publisher's retention and account behavior before using the history feature. <br>
Risk: The skill may store user and token data in a local workspace database. <br>
Mitigation: Run it in an isolated workspace when evaluating it and remove local workspace data after testing if the account context should not persist. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-plant-wilting-quantification-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [Plant Wilting API Documentation](references/api_doc.md) <br>
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown text containing structured JSON-style analysis, report links, and command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write analysis output to a user-specified local file.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
