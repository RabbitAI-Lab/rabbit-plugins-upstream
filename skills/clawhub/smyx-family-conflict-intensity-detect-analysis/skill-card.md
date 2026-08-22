## Description:

Using a fixed camera with microphone in the living room, the skill analyzes audio and video to estimate sound intensity, body-movement intensity, and family conflict intensity level as low, medium, or high.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to analyze consented living-room audio/video or URLs for structured conflict-intensity reports and gentle reminder guidance. It is intended as an auxiliary awareness and reporting tool, not as legal, therapeutic, or safety advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes highly sensitive household audio/video and may send media or URLs to a backend.

Mitigation: Use only with clear consent from every affected household member, and avoid bystander or minor recordings unless there is a lawful basis.

Risk: Reports may be associated with persistent identifiers and identity records may be stored locally.

Mitigation: Review identity and report-retention behavior before deployment, and define a deletion process for local records and remote reports.

Risk: Conflict-intensity results could be misused as determinations about legal, therapeutic, or personal safety status.

Mitigation: Present results only as auxiliary acoustic and visual indicators, and avoid using the skill as legal, therapeutic, or emergency-response advice.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-family-conflict-intensity-detect-analysis)
- [Skill API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis results with report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include acoustic metrics, visual metrics, conflict intensity level, alert type, gentle reminder text, suggested action, and history-report tables.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
