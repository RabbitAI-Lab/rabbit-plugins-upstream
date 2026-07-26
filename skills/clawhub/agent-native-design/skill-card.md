## Description: <br>
Use when designing, reviewing, or refactoring a CLI that must serve AI agents alongside humans, or when converting an API or SDK into an agent-usable CLI interface. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agents365-ai](https://clawhub.ai/user/agents365-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to evaluate, design, and refactor command-line interfaces so they work reliably for humans, AI agents, and orchestration systems. It helps review structured output, schema introspection, dry-run behavior, safety boundaries, delegated authentication, and recovery paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Advisory recommendations may be applied to CLIs that handle credentials or destructive operations. <br>
Mitigation: Review recommendations before implementation, preserve delegated authentication, and gate destructive commands with explicit safety boundaries. <br>
Risk: The skill may be auto-selected for relevant CLI-design prompts, so its guidance can influence interface contracts without a separate manual request. <br>
Mitigation: Treat generated reviews and refactor plans as proposals; validate them against the CLI's tests, schemas, and release requirements before deployment. <br>


## Reference(s): <br>
- [Agent Native Design on ClawHub](https://clawhub.ai/agents365-ai/skills/agent-native-design) <br>
- [Review Checklists](references/checklists.md) <br>
- [Design Patterns](references/design-patterns.md) <br>
- [Examples and Non-Examples](references/examples.md) <br>
- [Rubric](references/rubric.md) <br>
- [Testing an Agent-Native CLI](references/testing.md) <br>
- [When CLI vs MCP vs Both](references/hybrid-mcp-cli.md) <br>
- [Citations](references/citations.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with structured review sections, examples, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory output should be reviewed before applying recommendations to CLIs that handle credentials, write operations, or destructive actions.] <br>

## Skill Version(s): <br>
1.3.5 (source: server release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
