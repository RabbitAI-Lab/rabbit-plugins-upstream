## Description: <br>
Using a fixed camera installed above or beside a home medication area, this skill analyzes video to detect medication pickup, movement to mouth, and swallowing steps and records incomplete medication events for caregiver follow-up. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, elder-care operators, and developers use this skill to analyze medication-area videos for visual compliance signals, generate structured reports, and retrieve prior medication-compliance reports. The output supports caregiver follow-up and is not a substitute for medical advice or prescribed medication decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Medication-area videos and related identifiers may be processed by remote services and linked to persistent report history. <br>
Mitigation: Use only with clear consent from the monitored person or caregiver, confirm retention and access controls, and verify where videos, snapshots, reports, and identifiers are stored. <br>
Risk: Remote URL inputs may cause the service to fetch externally supplied media. <br>
Mitigation: Restrict submitted URLs to approved media locations and confirm the remote service enforces URL allowlists, size limits, and content validation. <br>
Risk: Automated medication-compliance analysis can be incomplete or wrong, especially when video quality does not show the pill box, hands, mouth, and neck clearly. <br>
Mitigation: Treat results as caregiver-support signals only, require human follow-up for missed or uncertain medication events, and do not use the output as medical advice. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-medication-compliance-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown text with structured JSON-style analysis results, compliance status, alert text, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save report output to a local file when an output path is provided.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
