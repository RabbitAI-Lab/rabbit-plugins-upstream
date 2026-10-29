## Description:

Helps managers maintain a Markdown-based record of team, company, and stakeholder context, turn conversations into traceable notes and follow-ups, and prepare reports and dashboards with optional Notion or FlowUs backup and sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jichengkai](https://clawhub.ai/user/jichengkai)

### License/Terms of Use:

MIT-0

## Use Case:

Managers use this skill to organize team and company notes, preserve and classify conversation evidence, track commitments, and prepare 1:1 meetings, performance materials, reports, and team dashboards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Team, performance, conversation, and company notes may contain sensitive information.

Mitigation: Limit access to local records and review what is recorded or shared.

Risk: Optional Notion or FlowUs sync copies sensitive notes into an online workspace.

Mitigation: Leave sync disabled unless needed, review workspace sharing, and use scoped tokens where possible.

Risk: Scheduled sync may retain an access token in macOS Keychain after setup.

Mitigation: Review scheduled sync and stored credentials when enabling or retiring the connection.

## Reference(s):

- [Team Memory release](https://clawhub.ai/jichengkai/skills/team-memory)
- [Usage guide](artifact/references/usage.md)
- [Management memory and conversation capture](artifact/references/management-memory.md)
- [Online notebook backup and sync](artifact/references/online-notebook-sync.md)
- [Team dashboard guide](artifact/references/team-dashboard.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Configuration instructions]

**Output Format:** [Markdown notes and reports; optional SVG dashboard and JSON export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records retain source links and verification status; optional online backup and sync.]

## Skill Version(s):

2.8.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
