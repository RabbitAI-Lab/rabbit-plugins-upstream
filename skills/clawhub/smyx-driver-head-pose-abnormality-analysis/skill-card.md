## Description: <br>
Analyzes in-cabin driver face video to estimate head pitch and yaw and report head-down or side-view distraction events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit driver-facing DMS video or a video URL for head-pose abnormality analysis, distraction-event reporting, and historical report lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Driver-face videos, video URLs, generated identity values, and report queries are sent to lifeemergence.com/open.lifeemergence.com cloud services. <br>
Mitigation: Use only with driver consent and an approved data-sharing basis, and avoid submitting videos that exceed the intended driver head-pose analysis use case. <br>
Risk: Generated report links and historical report lookups may expose sensitive driver monitoring records. <br>
Mitigation: Treat report links as sensitive, restrict access to report history, and avoid sharing exported report URLs outside authorized workflows. <br>
Risk: The skill may reuse or create local identity and token records, including the workspace smyx-api-key.txt identity file and local data database. <br>
Mitigation: Review or clear local workspace data after use when strict retention, credential, or account-separation controls are required. <br>


## Reference(s): <br>
- [Skill page](https://clawhub.ai/18072937735/skills/smyx-driver-head-pose-abnormality-analysis) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Skill usage demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-formatted analysis text with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured head-pose angles, distraction events, warning messages, recommended actions, and cloud report export links.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
