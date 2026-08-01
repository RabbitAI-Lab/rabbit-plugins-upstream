## Description: <br>
Analyzes authorized long-duration home camera video from bedroom and dining areas to report behavioral markers such as extended immobility, appetite-related activity changes, baseline comparisons, and caregiver-facing alerts without making a medical diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, community elder-care teams, and health-management platform operators can use this skill to analyze authorized 24-hour-or-longer home video for behavior-change reports covering bed time, eating activity, baseline deviation, and recommended follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Highly sensitive home video and identity-linked report data may be sent to external services. <br>
Mitigation: Use only with explicit consent from the monitored person and only for videos or URLs the user is authorized to submit. <br>
Risk: Local or backend identities may be created or reused automatically with limited user control. <br>
Mitigation: Review account handling before installation and avoid history or report-export functions unless the active account and data scope are understood. <br>
Risk: Behavioral changes may be mistaken for a clinical depression diagnosis. <br>
Mitigation: Present outputs as behavioral observations and caregiver prompts, and require qualified medical evaluation for diagnosis or treatment decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-depression-behavioral-markers-analysis) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Skill usage demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON-like structured report text with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include behavioral statistics, baseline comparisons, risk signal labels, caregiver guidance, report links, and historical report tables.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence; artifact frontmatter lists 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
