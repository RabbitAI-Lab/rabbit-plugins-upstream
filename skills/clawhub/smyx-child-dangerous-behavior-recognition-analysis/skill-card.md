## Description: <br>
Detects child hazardous behaviors such as climbing, playing with fire, touching power sources, and dangerous actions near windows, then returns alerts and structured safety analysis reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, caregivers, and operators use this skill to analyze child-monitoring video files or URLs for hazardous behaviors and to retrieve structured reports and report history. It is intended as an auxiliary child-safety monitoring tool, not as a substitute for human confirmation and intervention. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive child-monitoring videos or video URLs may be sent to the configured cloud service for analysis. <br>
Mitigation: Use the skill only with explicit consent, test with non-sensitive media first, and confirm the publisher's retention and deletion terms before using real monitoring footage. <br>
Risk: Report history is tied to an automatically resolved account and can expose prior child-safety analysis reports. <br>
Mitigation: Use a dedicated account for testing and restrict report-history access to authorized operators. <br>
Risk: Service tokens may be stored in a local workspace database. <br>
Mitigation: Run the skill in a controlled workspace, protect local storage, and rotate or remove credentials after evaluation. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/18072937735/skills/smyx-child-dangerous-behavior-recognition-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, files] <br>
**Output Format:** [Markdown or JSON analysis reports, optional saved output files, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports basic, standard, and JSON detail levels; local video files are limited to mp4, avi, and mov formats up to 10 MB.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
