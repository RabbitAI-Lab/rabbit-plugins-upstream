## Description:

Helps agents humanize AI-shaped text, draft or continue genre-aware prose, and audit long-form continuity while preserving voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whh110112](https://clawhub.ai/user/whh110112)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and editing agents use this skill to draft, continue, humanize, and review prose across genres while preserving source facts, author voice, and long-form continuity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Invoked workflows may read draft, source, reference, and ledger files in the configured workspace and write audit or manuscript outputs.

Mitigation: Use only workspaces whose files you are comfortable exposing to the skill, review the configured root paths, and keep backups of important drafts.

Risk: Optional HTTP MCP mode can expose local project coordination over a network.

Mitigation: Keep HTTP MCP bound to loopback or protect remote access with HTTPS and a bearer token.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/whh110112/skills/human-writing-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration, Files, JSON]

**Output Format:** [Prose and Markdown, with optional structured audit and configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include staged audit reports and conservative edit previews.]

## Skill Version(s):

0.17.0 (source: server release evidence, pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
