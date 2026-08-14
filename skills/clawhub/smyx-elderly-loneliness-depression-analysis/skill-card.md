## Description:

Using fixed cameras in homes or care settings, this skill analyzes daily elder activity video to detect behavior indicators such as dazing, sighing, and self-talking and generate behavior-based loneliness or depression-tendency risk reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, and community elder-care workers use this skill to analyze fixed-camera video or URL inputs for objective behavioral indicators, risk-level reports, care reminders, and historical report lookup. Outputs should be treated as behavior-based risk prompts, not as medical diagnosis, psychological scale scoring, or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive home video, optional audio, identity values, and report history may be sent to LifeEmergence backend services.

Mitigation: Use only with explicit informed consent from the elder and anyone recorded; confirm retention, access-control, and deletion practices before using real household footage.

Risk: Shared workspaces or default accounts may expose identity-linked analysis history.

Mitigation: Avoid shared workspaces and shared default accounts, and protect the workspace data directory used by the skill.

Risk: Behavior-based risk levels may be mistaken for a clinical diagnosis.

Mitigation: Present outputs as monitoring prompts only and route diagnosis, treatment, or urgent self-harm concerns to qualified professionals.

## Reference(s):

- [API interface documentation](artifact/references/api_doc.md)
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-loneliness-depression-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown reports and JSON analysis output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior metrics, risk levels, care reminders, history tables, and report links.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
