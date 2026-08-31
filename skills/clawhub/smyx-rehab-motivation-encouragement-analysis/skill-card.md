## Description:

Analyzes rehabilitation-session video and optional audio to detect frustration or giving-up tendency signals, produce structured findings, and suggest or trigger staged encouragement workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External rehab teams, care organizations, and agent operators can use this skill to analyze rehabilitation training media for frustration, interrupted training, low engagement, stalled progress, and related motivation signals. The skill returns structured reports and guidance intended to support encouragement workflows without making medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive rehabilitation video, optional audio, biometric identity binding, cloud reports, and retained history.

Mitigation: Deploy only in governed rehab settings with explicit patient consent for video/audio analysis, biometric identification, cloud upload, retained history, and report access.

Risk: Configured API endpoints and environment-specific settings can affect where patient media and reports are sent.

Mitigation: Review production API endpoints before installation and disable or remove dev/private-network configuration that is not appropriate for the deployment.

Risk: Encouragement workflows may notify therapists or family members and influence patient behavior.

Mitigation: Use the skill as behavioral support only, keep therapist oversight in the workflow, and avoid medical diagnosis or unsupervised training-plan changes.

Risk: Progress comparisons or encouragement messages can become misleading if they use inaccurate history or inappropriate wording.

Mitigation: Base progress feedback only on verified historical training records, avoid pressure-based comparisons, and use authorized standard TTS or pre-recorded voices rather than cloned voices.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-rehab-motivation-encouragement-analysis)
- [Rehab motivation API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON report content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud history, upload local media, or pass remote media URLs to configured API services.]

## Skill Version(s):

1.0.9 (source: server release evidence; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
