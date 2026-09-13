## Description:

Use when initializing or migrating an AI agent harness in a repository.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create or migrate a repository's AI-agent harness into a Claude Code-centered structure, including rules, memory, subagents, platform references, and validation artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent repository rules may override later user intent.

Mitigation: Review generated `.claude/rules/global-rules.md` before approval and remove or revise any rule that gives repository instructions precedence over user instructions.

Risk: Broad migration can move or delete existing harness files after the discovery gate.

Mitigation: Approve only after checking the migration plan, especially every planned move, merge, conversion, and deletion.

Risk: Generated memory, settings, hooks, or MCP-related artifacts may expose sensitive project context if committed without review.

Mitigation: Inspect generated `.claude/memory/`, `.claude/settings.json`, hooks, and MCP references, and avoid committing secrets, private credentials, or sensitive customer data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/create-agent-harness)
- [Publisher profile](https://clawhub.ai/user/afonsoft)
- [Source metadata URL](https://github.com/afonsoft/skills)
- [agents.md specification](https://agents.md/#examples)
- [OpenAI - Harness Engineering](https://openai.com/index/harness-engineering/)
- [Anthropic - Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [Claude Code - Memory and Imports](https://code.claude.com/docs/en/memory)
- [Claude Code - Subagents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code - Settings and Permissions](https://code.claude.com/docs/en/settings)
- [Claude Code - Hooks](https://code.claude.com/docs/en/hooks)
- [Claude Code - Slash Commands](https://code.claude.com/docs/en/slash-commands)
- [Devin CLI - Extensibility](https://docs.devin.ai/pt-BR/cli/extensibility)
- [Martin Fowler - Harness Engineering](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html)
- [LangChain - The Anatomy of an Agent Harness](https://blog.langchain.com/the-anatomy-of-an-agent-harness/)
- [Agent Skills Specification](https://agentskills.io/specification)
- [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro)
- [GitHub Agentic Workflows](https://github.com/github/gh-aw)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, file paths, configuration snippets, and generated repository files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended to be grounded in repository evidence and may include generated or migrated harness artifacts.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
