## Description:

Bootstrap or migrate a repository's agent harness into a Claude Code-centered structure with CLAUDE.md, .claude/ rules, sub-agents, skills, memory, validation, and thin platform references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to initialize or migrate repository-level AI agent harnesses, consolidate legacy agent files into .claude/, and produce validation-backed instructions, memory, rules, sub-agents, and platform references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill restructures agent-harness files and may move or remove legacy harness artifacts after confirmation.

Mitigation: Review the discovery summary and migration plan before approving changes, and verify the exact files marked for movement or removal.

Risk: Generated persistent rules may claim priority over future user instructions.

Mitigation: Review and edit generated global rules before deployment so repository policy does not override authorized future user direction.

Risk: The memory protocol creates durable, committed project documentation.

Mitigation: Treat memory files as shared documentation and avoid committing secrets, credentials, PII, customer identifiers, or sensitive operational details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/create-agent-harness)
- [Publisher profile](https://clawhub.ai/user/afonsoft)
- [Source URL from skill metadata](https://github.com/afonsoft/skills)
- [Context Engineering](references/context-engineering.md)
- [Memory Protocol](references/memory-protocol.md)
- [Migration Map](references/migration-map.md)
- [Platform Quirks](references/platform-quirks.md)
- [SPEC SDD Template](references/spec-sdd-template.md)
- [Validation Artifacts](references/validation-artifacts.md)
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

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, shell commands, JSON configuration, and repository files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces repository harness artifacts and a validation report after a human-confirmed discovery gate.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
