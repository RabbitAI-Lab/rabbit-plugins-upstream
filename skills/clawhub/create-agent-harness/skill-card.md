## Description:

Use when initializing or migrating an AI agent harness in a repository.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to initialize or migrate repository AI-agent harnesses into a Claude Code-centered structure. It guides discovery, migration, generated harness artifacts, memory, rules, sub-agents, specs, validation checks, and thin references for supported agent platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent agent rules and memory can materially affect future agent behavior and user control.

Mitigation: Run the skill only on a dedicated branch, inspect the discovery and migration plan before allowing writes, and review generated rules and memory before merging.

Risk: Legacy AGENTS, rules, memory, or settings content may contain prompt-injection instructions that would be migrated into the new harness.

Mitigation: Review legacy harness content before migration and remove or rewrite untrusted instructions before accepting generated artifacts.

Risk: MCP or settings files can reference credentials or sensitive configuration.

Mitigation: Do not copy credential values into context artifacts; reference where secrets are managed and keep secrets out of generated files.

Risk: Migration cleanup can remove legacy files with git rm.

Mitigation: Verify that useful content exists at the destination and review the cleanup diff before accepting deletions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/create-agent-harness)
- [Publisher metadata URL](https://github.com/afonsoft/skills)
- [Context Engineering](artifact/references/context-engineering.md)
- [Memory Protocol](artifact/references/memory-protocol.md)
- [Migration Map](artifact/references/migration-map.md)
- [Platform Quirks](artifact/references/platform-quirks.md)
- [SPEC SDD Template](artifact/references/spec-sdd-template.md)
- [Validation Artifacts](artifact/references/validation-artifacts.md)
- [Engineer sub-agent reference](artifact/references/agents/engineer.md)
- [Plan sub-agent reference](artifact/references/agents/plan.md)
- [Review sub-agent reference](artifact/references/agents/review.md)
- [Test sub-agent reference](artifact/references/agents/test.md)
- [agents.md specification](https://agents.md/#examples)
- [OpenAI Harness Engineering](https://openai.com/index/harness-engineering/)
- [Anthropic Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [Claude Code Memory and Imports](https://code.claude.com/docs/en/memory)
- [Claude Code Subagents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code Settings and Permissions](https://code.claude.com/docs/en/settings)
- [Claude Code Hooks](https://code.claude.com/docs/en/hooks)
- [Claude Code Slash Commands](https://code.claude.com/docs/en/slash-commands)
- [Devin CLI Extensibility](https://docs.devin.ai/pt-BR/cli/extensibility)
- [Martin Fowler Harness Engineering](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html)
- [LangChain Anatomy of an Agent Harness](https://blog.langchain.com/the-anatomy-of-an-agent-harness/)
- [Agent Skills Specification](https://agentskills.io/specification)
- [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro)
- [GitHub Agentic Workflows](https://github.com/github/gh-aw)
- [awesome-ai-conventions](https://github.com/GuilhermeAlbert/awesome-ai-conventions)
- [Awesome Harness Engineering](https://github.com/walkinglabs/awesome-harness-engineering)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, generated repository files, JSON configuration, and validation reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs as a phased repository workflow with a discovery gate before file creation, migration, or deletion.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
