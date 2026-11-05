## Description:

Prepare the session for context compaction - write a handoff file a fresh session can continue from, propose updates to the project's durable docs, apply them on approval or with `auto`. Use before compacting or clearing context, or on "pre-compact".

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and developers can run this skill before context compaction to preserve the current work in a handoff file and identify updates needed in the project's durable documentation. They can review proposed changes and approve them, or use `auto` to apply them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Proposed documentation changes or a persistent handoff reminder could introduce inaccurate guidance or affect future projects.

Mitigation: Review proposed changes before approval; assess the persistent reminder before adding it.

Risk: A handoff may contain sensitive conversation details.

Mitigation: Review the handoff for sensitive details before sharing or committing it.

## Reference(s):

- [Skill source repository](https://github.com/tenequm/skills/tree/main/skills/pre-compact)
- [ClawHub skill page](https://clawhub.ai/tenequm/skills/pre-compact)

## Skill Output:

**Output Type(s):** [Files, Markdown, Documentation guidance]

**Output Format:** [Markdown handoff file and proposed or applied documentation updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a time-stamped handoff file; documentation changes require approval unless `auto` is used.]

## Skill Version(s):

0.1.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
