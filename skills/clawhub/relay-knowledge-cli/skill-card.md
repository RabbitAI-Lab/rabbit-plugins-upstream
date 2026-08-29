## Description:

Relay Knowledge CLI guides agents through repository knowledge bootstrap, local CLI indexing, GraphRAG and code-map queries, and durable update/status/impact loops around commits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stevetdp](https://clawhub.ai/user/stevetdp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to initialize and validate repository knowledge maps, index local repositories, query code and business knowledge graphs, and refresh impact/context evidence after commits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents using this skill may index repository files and business glossary data into relay-knowledge's local runtime store.

Mitigation: Use the skill only for repositories and authored business data that are approved for local indexing.

Risk: Service installation, repository update, and worker commands may create or continue long-running local runtime work.

Mitigation: Review service-install commands before enabling them, inspect repo status for active tasks, and avoid starting competing workers.

## Reference(s):

- [Project homepage](https://github.com/coolplayagent/relay-knowledge)
- [ClawHub skill page](https://clawhub.ai/stevetdp/skills/relay-knowledge-cli)
- [Relay Knowledge CLI Workflows](references/cli-workflows.md)
- [Knowledge Map and Code Map Workflows](references/knowledge-map-workflows.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with JSON-oriented CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing workflow guidance for local repository indexing, querying, diagnostics, and update recovery.]

## Skill Version(s):

1.1.14 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
