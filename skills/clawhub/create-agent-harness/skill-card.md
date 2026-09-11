## Description:

Bootstraps or migrates a repository-wide agent harness with Claude-oriented instructions, settings, rules, subagents, memory, knowledge, hooks, validation, and thin references for supported agent platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to initialize or migrate repository agent harnesses, especially when consolidating legacy agent instructions into Claude Code-compatible structure with memory, rules, validation, and platform references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates persistent agent rules, settings, memory files, subagents, and optional hooks that can affect future agent behavior across the repository.

Mitigation: Review generated harness files before adoption, keep permissions narrowly scoped, and remove any rule or hook that is not needed for the repository.

Risk: A generated global rule could be written too broadly and conflict with later authorized user or maintainer instructions.

Mitigation: Revise global rules so they express repository guardrails without overriding future explicit human authorization.

Risk: A repository-wide formatter hook can make broad file changes after edits.

Mitigation: Remove the formatter hook or restrict it to known project file types and commands that are already used in the repository.

Risk: External research or WebFetch use by planning workflows can introduce unsourced or inappropriate guidance.

Mitigation: Require explicit approval for external research and require cited sources in generated plans and knowledge files.

Risk: Migration removes legacy harness structures after consolidating them into .claude.

Mitigation: Use the discovery gate and migration plan to confirm useful content has a destination before any legacy files are removed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/afonsoft/skills/create-agent-harness)
- [Publisher Source Repository](https://github.com/afonsoft/skills)
- [Context Engineering](references/context-engineering.md)
- [Memory Protocol](references/memory-protocol.md)
- [Migration Map](references/migration-map.md)
- [Platform Quirks](references/platform-quirks.md)
- [SPEC SDD Template](references/spec-sdd-template.md)
- [Validation Artifacts](references/validation-artifacts.md)
- [Agent Skills Specification](https://agentskills.io/specification)
- [Claude Code Memory](https://code.claude.com/docs/en/memory)
- [Claude Code Sub-agents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code Settings](https://code.claude.com/docs/en/settings)
- [Claude Code Hooks](https://code.claude.com/docs/en/hooks)
- [Claude Code Slash Commands](https://code.claude.com/docs/en/slash-commands)
- [Devin CLI Extensibility](https://docs.devin.ai/pt-BR/cli/extensibility)
- [Harness Engineering](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html)
- [Anatomy of an Agent Harness](https://blog.langchain.com/the-anatomy-of-an-agent-harness/)
- [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with shell command blocks and repository file templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or migrate persistent repository harness files after a discovery gate and validation pass.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
