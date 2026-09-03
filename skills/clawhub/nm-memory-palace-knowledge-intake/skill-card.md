## Description:

Processes external resources into stored knowledge with quality scoring and routing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and knowledge workers use this skill to evaluate external articles, papers, documents, and session outputs, then route valuable material into a structured knowledge corpus or related project updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can maintain a persistent knowledge corpus that may retain private URLs, local file paths, or sensitive research context.

Mitigation: Review generated entries before storage and remove private URLs, local paths, credentials, and sensitive context.

Risk: Evergreen knowledge can be promoted to GitHub Discussions by default.

Mitigation: Disable default publishing or require explicit yes-style confirmation before any GitHub post or update.

Risk: The skill can direct code, documentation, or skill changes without tight boundaries.

Mitigation: Run in a sandbox, avoid auto-accept, and require explicit approval before repository edits or knowledge pruning.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-memory-palace-knowledge-intake)
- [OpenClaw metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/memory-palace)
- [KonMari Method](https://konmari.com/about-the-konmari-method/)
- [Spark Joy Philosophy](https://konmari.com/marie-kondo-rules-of-tidying-sparks-joy/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured evaluation notes, example code, shell commands, and configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose persistent corpus entries, GitHub Discussion publication, repository edits, and pruning actions that require human review.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
