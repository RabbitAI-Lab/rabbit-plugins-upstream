## Description:

Using fixed-camera home or private nursing-room video, with optional audio, this skill analyzes elder activity for loneliness-related behavior signals and returns a structured loneliness index, level, warm-companionship recommendations, caregiver summaries, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, elder-care platform operators, and developers use this skill to analyze consented video or video URLs from solitary-living elder-care settings, review behavioral loneliness signals, and produce companionship or caregiver follow-up recommendations. It is not a medical diagnostic tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive in-home or nursing-room video and optional audio may be uploaded or referenced through remote services.

Mitigation: Use only with explicit consent from the monitored elder and relevant caregivers, confirm the remote service and retention terms before deployment, and prefer privacy-preserving modes such as body-outline or face-masking where available.

Risk: The skill may query cloud report history and create or reuse persistent local identity, token, or profile data.

Mitigation: Run it in an isolated environment, restrict access to local account data, avoid shared machines for sensitive deployments, and remove or rotate stored credentials when the skill is no longer needed.

Risk: Automatic companionship actions and caregiver notifications can affect an elder's autonomy or create distress if triggered incorrectly.

Mitigation: Require caregiver review for deployment, preserve the elder's ability to turn off reminders, limit intervention frequency, and treat reports as behavioral signals rather than medical diagnoses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-loneliness-comfort-analysis)
- [API interface documentation](artifact/references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown status text with structured JSON report content, caregiver-facing recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the rendered report text to a local output file when an output path is provided.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
