## Description:

Analyzes rehabilitation training images or video to detect patient frustration or giving-up tendency signals and produce structured motivation, escalation, and report guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External rehabilitation teams and authorized caregivers use this skill to analyze patient training media for behavioral signs of frustration or giving-up tendency, produce structured reports, and surface encouragement or escalation suggestions. It is framed as behavioral support and does not provide medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive patient media may be transmitted to cloud analysis services.

Mitigation: Use only in authorized rehab or healthcare environments with documented patient consent, approved cloud-processing terms, endpoint allowlisting, retention limits, and audit logging.

Risk: Silent identity creation and local token persistence may reduce user-facing control over account state.

Mitigation: Review identity provisioning, local token storage, credential rotation, and deletion procedures before use with real patient media.

Risk: Therapist or family notifications and encouragement actions may affect patient care workflows.

Mitigation: Require clear operational approval for notification recipients, escalation thresholds, audio playback, and any therapist or family involvement.

Risk: Behavioral outputs could be mistaken for medical diagnoses or treatment changes.

Mitigation: Present outputs as behavioral observations and motivation guidance only, and require clinician confirmation for diagnosis, treatment, or exercise-intensity changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-rehab-motivation-encouragement-analysis)
- [Rehab motivation API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, files, guidance]

**Output Format:** [Markdown-formatted text with structured JSON payloads, CLI commands, report links, and optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local mp4, avi, or mov files and video URLs; local file analysis is limited to 10 MB.]

## Skill Version(s):

1.0.6 (source: server release evidence; artifact frontmatter lists 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
