## Description:

Create custom subagents for specialized AI tasks, including task-specific agents, code reviewers, debuggers, and domain-specific assistants with custom prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design persistent subagent prompt files for project-level or user-level assistants. It guides the creation of focused agent descriptions, YAML frontmatter, and system prompts for specialized workflows such as code review, debugging, and data analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill helps create persistent subagent prompt files whose behavior may continue to affect future agent sessions.

Mitigation: Review generated subagent prompts before deployment and prefer project-level agents for codebase-specific behavior.

Risk: Broad proactive descriptions can trigger delegation more often than intended.

Mitigation: Keep descriptions specific, scoped to the intended workflow, and review trigger language before sharing the agent.

Risk: Example agents may reference external tools such as BigQuery.

Mitigation: Add explicit scope, authorization, and data-handling rules before using tool-oriented examples.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with YAML frontmatter examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance and example subagent prompt files; it does not execute code directly.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
