## Description: <br>
Analyzes fixed-camera living-room video to estimate whether an older adult is sitting and watching TV, track continuous viewing duration, and produce a friendly movement reminder when the configured sedentary threshold is exceeded. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Caregivers, elderly-care service operators, and developers use this skill to analyze sofa-and-TV-area video or report history for prolonged TV-watching posture and activity reminders. It supports structured reports, reminder text, and cloud report links, but should not be treated as medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may upload or fetch sensitive in-home video and store or query video-derived reports in a cloud service. <br>
Mitigation: Use only with clear consent from the monitored person or caregiver; verify retention, access controls, encryption, and report sharing before deployment. <br>
Risk: Reports can be linked to an internal identity and later queried or exported. <br>
Mitigation: Restrict access to authorized caregivers or administrators, protect stored tokens, and avoid exposing internal identity values in user-facing output. <br>
Risk: The security verdict is suspicious because the workflow depends on a remote lifeemergence service for sensitive video-derived reports. <br>
Mitigation: Install only if the publisher and remote service are trusted, and test with non-sensitive samples before using real household or care-facility video. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-tv-sedentary-reminder-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface reference](artifact/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports and tables with JSON structured analysis content, reminder text, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save report output to a file when an output path is provided; history queries return cloud report links.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence; artifact frontmatter says 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
