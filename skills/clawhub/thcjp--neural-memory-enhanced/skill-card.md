## Description:

神经记忆增强系统 helps agents persist and recall conversation-derived memories through a local associative memory graph with spreading activation, typed links, lifecycle decay, conflict marking, snapshots, and cross-brain transfer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to give coding or workflow agents long-lived local memory for project decisions, preferences, errors, facts, and context, then recall related information through graph traversal during later sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill encourages long-lived local storage of conversation-derived facts, decisions, preferences, errors, and dialogue text without a clear opt-in, deletion, or sensitivity-control flow.

Mitigation: Enable it only for approved projects, avoid secrets, regulated data, confidential business discussions, and personal information, and define review, deletion, and project-isolation rules before use.

Risk: Persisted local memories can preserve outdated, incorrect, or conflicting information that later influences agent behavior.

Mitigation: Review recalled memories before acting, use conflict annotations and snapshots, and prune or correct stale memories when decisions change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/neural-memory-enhanced)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to persist and recall local memory entries; outputs can include memory records, activation paths, conflict annotations, snapshot IDs, and configuration snippets.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter reports 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
