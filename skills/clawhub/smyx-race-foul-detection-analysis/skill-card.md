## Description:

Analyzes pet race start and finish videos to identify start timing, lane assignment, finish order, false starts, and lane-crossing fouls for referee review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External event operators, referees, trainers, and developers use this skill to submit pet racing video URLs or files for cloud-assisted foul detection and structured race reports. It supports objective review of false starts, lane crossing, lane assignment, and finish order, with final decisions remaining with event officials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends video files or video URLs to a Life Emergence cloud service for analysis.

Mitigation: Use only media that the operator is authorized to upload, and review provider privacy, retention, and data handling terms before installation.

Risk: The skill can create or reuse an internal identity, send that identity to the backend, and store returned credentials in a shared local SQLite database.

Mitigation: Run the skill in an isolated environment, restrict local database access, and clear stored credentials when deprovisioning or rotating users.

Risk: The skill can query cloud-stored report history associated with the internal identity.

Mitigation: Confirm report-history access controls and avoid using the skill where identity-linked media analysis history must not be retained by the provider.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-race-foul-detection-analysis)
- [API interface documentation](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown tables, JSON-style structured reports, report links, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud-hosted report links and history lists returned by the provider service.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
