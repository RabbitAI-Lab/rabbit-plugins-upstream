## Description: <br>
Analyzes in-cabin DMS camera media to estimate driver head pose, detect sustained head-down or side-view behavior, and return distracted-driving alerts with structured report output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, fleet operators, and developers use this skill to analyze driver-facing camera images, videos, or media URLs for head-pose abnormalities and distracted-driving events. It returns structured detection results, warning messages, recommended vehicle or fleet actions, and report links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Driver or cabin media and submitted URLs may be processed by a remote LifeEmergence service. <br>
Mitigation: Use the skill only with explicit driver or employee consent, and avoid submitting footage that is not approved for cloud processing. <br>
Risk: The skill may create or reuse account identity and retrieve account-linked report history without a clear user consent boundary. <br>
Mitigation: Deploy only in environments where silent account linkage is acceptable, and review who can query historical reports before installation. <br>
Risk: Authentication data may be stored locally for reuse. <br>
Mitigation: Install in a controlled workspace, restrict local file access, and remove persisted account data when decommissioning the skill. <br>
Risk: Head-pose detection can be unreliable when the driver face or head contour is not clearly visible. <br>
Mitigation: Use sufficiently clear DMS footage that meets the stated frame-rate, resolution, and visibility constraints, and treat alerts as driver-assistance signals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-driver-head-pose-abnormality-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/18072937735) <br>
- [Driver head-pose API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown text with structured JSON report content, warning summaries, report links, and optional command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local media files or media URLs; analysis and report history depend on remote LifeEmergence services and account-linked state.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
