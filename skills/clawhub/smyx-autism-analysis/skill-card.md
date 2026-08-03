## Description: <br>
Performs special video analysis on behavioral characteristics of children with autism, identifies core symptom features, provides structured analysis reports and intervention recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Parents, educators, professionals, and agent users can use this skill to analyze child video or image inputs for preliminary ASD-related behavioral characteristics, generate structured reports, and retrieve prior analysis reports. It is a screening and reporting aid, not a substitute for professional medical diagnosis or clinical evaluation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive child-related videos, images, autism reports, and report history may be processed by remote lifeemergence.com services. <br>
Mitigation: Use only media that the user is authorized to submit, start with non-sensitive test media, and review data handling expectations before installation or execution. <br>
Risk: The skill can create and persist local account state, including account identifiers and tokens, in the workspace data directory. <br>
Mitigation: Avoid manually passing hidden identity parameters, review local workspace data after use, and delete retained state when persistent account linkage is not desired. <br>
Risk: ASD analysis reports can be mistaken for medical diagnosis or clinical evaluation. <br>
Mitigation: Present outputs as preliminary screening information and direct users to qualified medical professionals for diagnosis or clinical decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-autism-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [smyx_analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown and JSON-formatted structured analysis reports with optional report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports mp4, avi, and mov inputs up to 10 MB; can save results to a file and list historical reports.] <br>

## Skill Version(s): <br>
1.0.9 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
