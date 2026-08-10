## Description:

Analyzes elderly nighttime bedroom camera video and audio to detect sudden sitting up, screams, and arm thrashing, then returns event timing, frequency, duration, and caregiver-oriented guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, and developers use this skill to analyze infrared bedroom sleep recordings or video URLs for abnormal startle or nightmare-like events and generate structured reports for care review. The outputs are behavioral event summaries and should not be treated as medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bedroom audio/video or video URLs may be processed through vendor cloud services.

Mitigation: Use only footage collected with explicit consent, avoid unrelated sensitive footage, and review the vendor's storage and report-retention practices before deployment.

Risk: The skill automatically associates reports with a managed account identity and may persist account tokens locally.

Mitigation: Review account and token handling before installation, restrict access to the workspace data directory, and clear stored credentials when the skill is no longer approved for use.

Risk: Sleep-event summaries could be mistaken for clinical diagnosis or treatment advice.

Mitigation: Present outputs as behavioral event statistics only, keep medication decisions outside the skill workflow, and route frequent or suspected RBD patterns to a qualified sleep or neurology clinician for PSG-based evaluation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-nightmare-startle-detect-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Elderly Nightmare Startle API Documentation](references/api_doc.md)
- [Common Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with JSON report content, event summaries, and optional report export links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured sleep-event fields, history-query results, and links to generated reports.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter and release changelog mention 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
