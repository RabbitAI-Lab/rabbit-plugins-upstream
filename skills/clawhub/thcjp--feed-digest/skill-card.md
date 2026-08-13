## Description:

Provides feed digest generation, transparent feed fetching, and read-status management for subscription sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to summarize RSS, Atom, and other subscription feeds, classify feed items, and manage read status inside an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports broad local file access, command execution, external API use, scheduling authority, and possible state updates.

Mitigation: Install only after reviewing the skill carefully, and restrict commands, file paths, API destinations, storage, and triggering behavior to feed retrieval, digest generation, and explicit read-status updates.

Risk: The security verdict is suspicious because the requested authority is not tightly scoped to a simple subscription digest.

Mitigation: Prefer a constrained release or run the skill in a sandboxed agent environment with explicit approval for file writes, command execution, and network/API access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/feed-digest)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON response examples and shell configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include feed digest data, metadata, execution logs, and read-status updates.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
