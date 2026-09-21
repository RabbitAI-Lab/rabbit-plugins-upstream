## Description:

Cross-session memory recovery for AI agents that keeps identity, rules, todos, and handover state available while using a local change index to avoid redundant rereads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ccy123abcd](https://clawhub.ai/user/ccy123abcd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to recover local working memory at the start of a new agent session, refresh handover notes, restate user rules, and optionally check actions against locally stored prohibitions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks an agent to read local memory files at session start.

Mitigation: Review the discovered paths before use and avoid broad must_read_extra entries.

Risk: The skill maintains local .changsheng state files for discovery, indexing, rules, and handover.

Mitigation: Inspect generated state files in the workspace and keep sensitive memory sources scoped to files the agent is intended to read.

Risk: The optional PreToolUse hook can block actions based on user-rule matches.

Mitigation: Enable the hook only when action blocking is desired, and review the extracted .changsheng/rules.json rules before relying on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ccy123abcd/skills/changsheng-agent-memory)
- [README](README.md)
- [Skill instructions](SKILL.md)
- [Example configuration](config.example.yaml)
- [Agent startup snippet](assets/agents-snippet.md)
- [Handover template](assets/handover-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local memory recovery guidance and may create or update local state files when the agent follows the skill.]

## Skill Version(s):

0.6.0 (source: frontmatter, changelog, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
