## Description:

Using a fixed camera with microphone in the living room, the skill analyzes audio and video to estimate sound intensity, body movement intensity, and family conflict intensity level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze household audio/video or video URLs for low, medium, or high conflict intensity, generate structured reports, and review cloud history for prior analyses. It is intended as an auxiliary awareness and reporting tool, not as legal, safety, or clinical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Household audio/video or video URLs may be sent to remote services for processing.

Mitigation: Use only with explicit consent from affected household members and only when remote processing of sensitive household media is acceptable.

Risk: The skill may create or reuse an internal identity, store account tokens locally, and query identity-linked cloud history.

Mitigation: Review identity and local token handling before installation, restrict access to the runtime environment, and clear stored credentials or reports when no longer needed.

Risk: Conflict-intensity outputs can be mistaken for legal, safety, or clinical determinations.

Mitigation: Treat outputs as auxiliary indicators only; do not use them to label parties, automate police reporting, or replace qualified legal, safety, or mental-health support.

## Reference(s):

- [API Documentation](artifact/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-family-conflict-intensity-detect-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown text with structured JSON-style analysis fields, report status messages, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include conflict intensity levels, acoustic and visual metrics, gentle reminder text, recommended actions, and history-report links.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
