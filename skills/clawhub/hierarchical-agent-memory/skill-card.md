## Description:

Organizes OpenClaw's long-term memory into a compact routing table, project and contact files, daily notes, and optional chronological summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[richgoodson](https://clawhub.ai/user/richgoodson)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use this skill to keep project and contact context organized across sessions, with optional scheduled summaries for historical recall.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent memory files may expose secrets or sensitive personal information in later agent sessions.

Mitigation: Keep credentials and sensitive personal data out of memory files; review stored project and contact information before use.

Risk: Reorganizing existing MEMORY.md content during migration may change or lose important context.

Mitigation: Review the proposed migration plan and approve changes to existing files before applying them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/richgoodson/skills/hierarchical-agent-memory)
- [Configuration reference](references/configuration.md)
- [Onboarding guide](references/onboarding-guide.md)
- [Migration guide](references/migration-v2-to-v3.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions, Files]

**Output Format:** [Markdown memory files and JSON configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional scheduled weekly, monthly, and yearly summaries; requires OpenClaw 2026.4.x or later and the memory-core plugin.]

## Skill Version(s):

3.1.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
