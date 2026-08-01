## Description: <br>
Analyzes office workstation video to detect prolonged sitting and posture issues such as forward head angle and back curvature, then returns structured alerts and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, workplace health teams, and developers use this skill to submit office workstation videos or URLs for posture and prolonged-sitting analysis, review structured warning messages, and query historical workplace health reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Employee or workspace video may be sent to the LifeEmergence backend and historical reports may be queryable. <br>
Mitigation: Use only with clear employee notice and consent, privacy review, retention controls, and access controls for report history. <br>
Risk: The skill creates or reuses persistent local identities and stores tokens for workplace monitoring data. <br>
Mitigation: Run with tenant and user isolation, restrict workspace data access, and clear local identity or token storage when no longer required. <br>
Risk: Posture alerts and health guidance may be mistaken for medical diagnosis or treatment advice. <br>
Mitigation: Present results as visual posture and activity monitoring only, and direct users with neck or back symptoms to qualified medical professionals. <br>


## Reference(s): <br>
- [API interface documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill usage demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-office-worker-posture-warning-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, files, guidance] <br>
**Output Format:** [Markdown text with structured JSON-like analysis, warning messages, and report links; optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May upload local video files or submit video URLs to a cloud analysis service and query historical reports.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
