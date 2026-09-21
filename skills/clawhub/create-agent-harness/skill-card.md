## Description:

Use when initializing or migrating an AI agent harness in a repository.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to initialize or migrate repository agent harnesses into a Claude-oriented structure with repository instructions, rules, skills, sub-agents, memory, specs, settings, and validation checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent memory may store prompt summaries and session decisions in repository files that are committed and shared.

Mitigation: Review the memory policy before installation, especially for confidential or regulated repositories; consider making memory opt-in, redacted, and limited to durable engineering decisions.

Risk: The skill is designed to rewrite or migrate agent harness files and remove legacy harness structures.

Mitigation: Run it on a dedicated branch, review the discovery gate and migration plan before approving writes, and inspect the validation report before merging.

Risk: Installed sub-agents and harness rules encourage broad proactive agent activity.

Mitigation: Review generated sub-agent descriptions, permissions, hooks, and settings before use; disable roles or automation that do not match the repository's governance model.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/create-agent-harness)
- [Project metadata URL](https://github.com/afonsoft/skills)
- [Context Engineering](references/context-engineering.md)
- [Memory Protocol](references/memory-protocol.md)
- [Migration Map](references/migration-map.md)
- [Platform Quirks](references/platform-quirks.md)
- [SPEC SDD Template](references/spec-sdd-template.md)
- [Validation Artifacts](references/validation-artifacts.md)
- [validate-harness.sh](scripts/validate-harness.sh)
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

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and repository file changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces or migrates repository harness artifacts, then validates them with deterministic checks.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata; artifact frontmatter version is 2.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
