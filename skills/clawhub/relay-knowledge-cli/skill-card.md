## Description:

Use relay-knowledge local CLI for repository CodeSpec/Knowledge map governance and GraphRAG: initialize, validate, route, and update codespec/codespec-map.yaml and knowledge/knowledge-map.yaml; read snapshot-bound repo business/software/view/context models for specs and coding; run durable update/status/impact loops after commits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stevetdp](https://clawhub.ai/user/stevetdp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to operate the relay-knowledge CLI for repository indexing, graph-backed code search, knowledge map governance, business glossary queries, software relationship queries, diagnostics, and commit-driven update loops.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release commonly relies on installing a mutable external CLI before use.

Mitigation: Use a pinned, verified release or previously audited binary, and review the version, source, destination, and permissions before allowing installation or upgrade.

Risk: The CLI can index local repository contents and maintain durable local knowledge state.

Mitigation: Run it only on trusted repositories and scopes, review commands before execution, and use an explicit temporary RELAY_KNOWLEDGE_HOME for smoke checks that should not touch existing state.

## Reference(s):

- [Relay Knowledge CLI Skill README](artifact/README.md)
- [Relay Knowledge CLI Workflows](artifact/references/cli-workflows.md)
- [Knowledge Map and Code Map Workflows](artifact/references/knowledge-map-workflows.md)
- [Relay Knowledge Map v4 artifacts schema](artifact/references/knowledge-map.schema.json)
- [Relay CodeSpec Map v4 root schema](artifact/references/codespec-map.schema.json)
- [Relay Knowledge Business Glossary v1 schema](artifact/references/business-glossary.schema.json)
- [Project homepage](https://github.com/coolplayagent/relay-knowledge)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with shell command examples and JSON-oriented CLI handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to run a local CLI that indexes repository contents and maintains durable local knowledge state.]

## Skill Version(s):

1.1.17 (source: SKILL.md frontmatter metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
