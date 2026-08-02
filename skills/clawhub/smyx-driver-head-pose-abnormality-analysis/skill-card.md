## Description: <br>
This skill analyzes in-cabin DMS driver video to detect head-down and side-view posture abnormalities and produce distracted-driving alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External fleet operators, vehicle safety teams, and developers use this skill to analyze driver-facing DMS videos or video URLs for head pose events, distracted-driving alerts, structured reports, and report history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Driver-facing videos and video URLs may contain biometric or workplace surveillance data and are sent to external LifeEmergence services for analysis. <br>
Mitigation: Use only with informed consent, an acceptable data-retention policy, and approval for the external service endpoint before processing real drivers or fleet footage. <br>
Risk: Cloud report history is associated with internal identity, account, and token flows that are mostly automatic. <br>
Mitigation: Confirm account ownership, access controls, and report visibility before enabling history queries in shared or fleet environments. <br>
Risk: The scanner verdict is suspicious because the skill handles sensitive driver footage without enough user control. <br>
Mitigation: Review the skill and its configuration before installation, restrict use to approved deployments, and avoid using it where consent or report-access practices are unclear. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-driver-head-pose-abnormality-analysis) <br>
- [API reference](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON structured analysis reports, report links, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report-history results and exported report-image links.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence; artifact frontmatter lists 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
