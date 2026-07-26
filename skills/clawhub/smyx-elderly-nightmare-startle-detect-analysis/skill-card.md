## Description: <br>
Using a fixed bedroom camera with infrared night vision and microphone input, this skill analyzes elderly nighttime sleep media to detect sudden sitting-up, short screams, arm-thrashing, and related abnormal sleep events, then records event timing, frequency, and duration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, caregivers, and care-platform developers use this skill to turn bedroom sleep video or video URLs into structured abnormal-event reports for elderly nighttime monitoring. The output is intended as behavioral reference material for care review and medical consultation, not as a medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive bedroom video, audio, or media URLs may be sent to external Life Emergence/Open API services. <br>
Mitigation: Use only with explicit consent from the recorded person and confirm the provider's data handling, retention, and deletion practices before deployment. <br>
Risk: The skill may silently create or reuse an internal user identity, associate reports with that identity, and store access tokens in a local SQLite database. <br>
Mitigation: Review identity handling and local credential storage before installation; restrict filesystem access and rotate or remove tokens when access is no longer needed. <br>
Risk: Sleep event labels and risk signals could be mistaken for medical diagnosis or treatment guidance. <br>
Mitigation: Present outputs as behavioral observations only and route frequent or concerning patterns to qualified neurology or sleep-medicine professionals for clinical evaluation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-nightmare-startle-detect-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-formatted analysis reports, with optional saved output files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include event timelines, frequency summaries, sleep-continuity scores, risk signal labels, family-facing summaries, recommendations, and report links.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
