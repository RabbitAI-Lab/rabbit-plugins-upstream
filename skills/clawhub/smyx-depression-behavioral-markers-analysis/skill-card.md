## Description:

Analyzes fixed home-camera video from bedroom and dining areas to report long immobility, appetite-related behavior changes, and caregiver-facing alerts without making medical diagnoses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, community care teams, and developers use this skill to analyze 24-hour-or-longer fixed-camera home video for sustained bed rest and reduced eating behavior signals. The skill produces observation reports and alerts for follow-up, not depression diagnosis, scoring, medication advice, or treatment planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Highly sensitive in-home health video may be uploaded or remotely processed.

Mitigation: Install only with the monitored person's informed consent, use a trusted provider, and confirm retention, access, and deletion terms before use.

Risk: The skill may silently create or reuse an internal identity and store service tokens locally.

Mitigation: Run it in a dedicated environment, inspect local identity and token storage, and clear or revoke credentials when the skill is no longer needed.

Risk: Behavioral markers can be mistaken for a medical diagnosis.

Mitigation: Use outputs only as observation aids and route concerning signals to family, community care staff, or licensed clinicians for interpretation.

Risk: Continuous bedroom and dining-area monitoring can expose intimate personal routines.

Mitigation: Prefer privacy-preserving modes such as human silhouettes, face masking, metric-only retention, and minimized access to raw recordings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-depression-behavioral-markers-analysis)
- [Depression behavioral markers API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown reports and JSON-formatted analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report export links and API-backed history listings; reliable alerts require 24h+ bedroom and dining-area video plus a 7-14 day personal baseline.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
