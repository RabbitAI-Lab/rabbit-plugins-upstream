## Description:

Emotion-linked memory recall, self-state, subjective journal, and identity continuity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to preserve and recall emotion-linked experience memory, self-state snapshots, subjective journals, and identity-continuity checks through OpenClaw and Notion-backed workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store emotional, journal, and identity-like material in Notion.

Mitigation: Install it only for agents that intentionally need this memory behavior, scope the Notion integration to the required parent page or databases, and define retention and deletion expectations before use.

Risk: Broad write paths and scheduled or ambient recall flows can persist or surface sensitive context unexpectedly.

Mitigation: Review cron and ambient recall settings per installation, keep ambient recall disabled with SIS_AMBIENT_RECALL=0 when it is not wanted, and require explicit acknowledgment only after a candidate is actually used.

Risk: Using an untrusted NOTIONCTL_PATH or installing dependencies through an unpinned @latest command can change what code handles Notion access.

Mitigation: Use only a trusted notionctl path and pin installer or dependency versions in production environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/soul-in-sapphire)
- [Publisher profile](https://clawhub.ai/user/nextaltair)
- [Soul memory boundaries and recall observation](references/memory-transition.md)
- [Bounded emotion-linked experience recall](references/experience-recall.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payloads and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and write Notion memory, journal, state, and local ambient recall files when configured with Notion credentials and database IDs.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
