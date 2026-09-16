## Description:

Use when initializing or migrating an AI agent harness in a repository.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to initialize or migrate a repository's AI agent harness into a Claude Code-centered structure with supporting rules, memory, subagents, platform references, and validation checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create persistent always-on rules and memory files that affect future agent sessions.

Mitigation: Review generated rules and memory before adoption; make prompt logging opt-in and subordinate to current user instructions.

Risk: Migration steps can remove legacy agent files after moving or converting them.

Mitigation: Run the discovery gate and confirm useful content exists at the destination before deletion; keep version-control history available for recovery.

Risk: Generated harness files may preserve summarized prompt history across sessions.

Mitigation: Apply repository privacy policy to memory content and redact secrets, sensitive prompts, and personal data before committing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/create-agent-harness)
- [Metadata URL](https://github.com/afonsoft/skills)
- [Context Engineering](artifact/references/context-engineering.md)
- [Memory Protocol](artifact/references/memory-protocol.md)
- [Migration Map](artifact/references/migration-map.md)
- [Platform Quirks](artifact/references/platform-quirks.md)
- [SPEC SDD Template](artifact/references/spec-sdd-template.md)
- [Validation Artifacts](artifact/references/validation-artifacts.md)
- [Claude Code Memory and Imports](https://code.claude.com/docs/en/memory)
- [Claude Code Subagents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code Settings](https://code.claude.com/docs/en/settings)
- [Claude Code Hooks](https://code.claude.com/docs/en/hooks)
- [agents.md Specification](https://agents.md/#examples)
- [Agent Skills Specification](https://agentskills.io/specification)
- [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro)
- [OpenAI Harness Engineering](https://openai.com/index/harness-engineering/)
- [Anthropic Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown files, JSON configuration, shell commands, and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or migrate repository harness files and validation artifacts after the discovery gate.]

## Skill Version(s):

1.0.9 (source: server release metadata; source skill metadata lists 2.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
