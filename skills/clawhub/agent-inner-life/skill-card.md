## Description:

Keeps a dated record of how an agent's work has been going, including an evening journal, night reflections, recall over prior stretches, local files under inner-life/, and a short native-memory summary injected into later sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dkistenev](https://clawhub.ai/user/dkistenev)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill when they want an agent to keep a durable local record of how work is going, refresh a short carry-forward memory summary, and answer later questions from the written record instead of reconstructing events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persists local journal, state, and dream files under inner-life/ and does not delete them when the skill is removed.

Mitigation: Enable it only when durable local continuity is desired, restrict access on shared hosts, and delete inner-life/ manually when the record should be removed.

Risk: The native-memory summary is visible to later sessions and may carry information into unrelated work.

Mitigation: Keep the summary short, work-focused, and free of secrets, confidential content, personal details, and third-party details; clear the memory summary when disabling the record.

Risk: Recall can expose local records to the current conversation, which may be inappropriate on shared or multi-user hosts.

Mitigation: Answer only from relevant entries, avoid unrelated journal material, and confirm access expectations before using the skill where multiple users share the same agent environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dkistenev/skills/agent-inner-life)
- [Project homepage](https://github.com/DKistenev/agent-inner-life)
- [State reference](references/state.md)
- [Journal reference](references/journal.md)
- [Dreams reference](references/dreams.md)
- [Recall reference](references/recall.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, configuration, guidance]

**Output Format:** [Markdown files, concise text answers, and a short native-memory summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local inner-life/ records and replaces a small native-memory summary when the relevant mode is run.]

## Skill Version(s):

1.2.2 (source: evidence.release.version and artifact/SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
