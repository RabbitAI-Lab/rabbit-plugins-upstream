## Description:

Guides agents through repository-specific Oracle-X development tasks, including FastAPI endpoints, upstream health integrations, blockchain adapters, prompts, LLM-backed notes, and the repository's test and build gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yigtwxx](https://clawhub.ai/user/yigtwxx)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill when changing the Oracle-X financial terminal codebase. It provides repository-specific guidance for endpoints, upstream data sources, blockchain adapters, LLM prompts, testing, and release checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is specific to the Oracle-X repository and may give incorrect guidance for other FastAPI, Next.js, blockchain, or LLM projects.

Mitigation: Use it only when working on Oracle-X and verify recommendations against the current repository files.

Risk: Generated guidance may affect authentication, upstream-health reporting, financial-data semantics, or LLM behavior.

Mitigation: Run the documented backend, frontend, agent-skill, and repo-facts checks before committing changes.

## Reference(s):

- [Oracle-X repository](https://github.com/Yigtwxx/OracleX)
- [Oracle-X agent skill source](https://github.com/Yigtwxx/OracleX/tree/main/agent-skill)
- [Adding a backend endpoint](references/endpoint.md)
- [Adding an upstream data source](references/upstream.md)
- [Adding a blockchain](references/chains.md)
- [Prompts, the model chain, and notes](references/llm.md)
- [Testing](references/testing.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code and bash command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Repository-specific conventions and quality-gate guidance for Oracle-X.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter lists 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
