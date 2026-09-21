## Description:

Relay Knowledge CLI helps agents operate the relay-knowledge local CLI to index repositories, query CodeSpec and Knowledge Map artifacts, use GraphRAG views, and refresh repository knowledge after commits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stevetdp](https://clawhub.ai/user/stevetdp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to bootstrap repository knowledge maps, run graph-backed code and business-knowledge queries, and keep local repository knowledge current during coding and commit workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository indexing can place sensitive repository contents in the local relay-knowledge store.

Mitigation: Register only the narrow repository path needed for the task and use an explicit temporary RELAY_KNOWLEDGE_HOME for isolated tests.

Risk: The skill may update repository knowledge-map or glossary files when requested.

Mitigation: Review generated file changes, run relay-knowledge map validation, and avoid direct edits to generated map roots unless the CLI is unavailable and the user explicitly authorizes manual repair.

Risk: Optional service behavior can perform persistent background indexing.

Mitigation: Enable or install the local service only when persistent indexing is desired, and use status and doctor commands to confirm active task state.

Risk: Downloaded CLI binaries can carry supply-chain risk if fetched from an unverified source.

Mitigation: Use a published source, verify the downloaded binary, and preserve proxy settings during download and checksum verification.

## Reference(s):

- [Relay Knowledge homepage](https://github.com/coolplayagent/relay-knowledge)
- [Relay Knowledge CLI workflows](references/cli-workflows.md)
- [Knowledge Map and Code Map workflows](references/knowledge-map-workflows.md)
- [Type calls and configuration evidence](references/language-capabilities.md)
- [Knowledge Map schema](references/knowledge-map.schema.json)
- [CodeSpec Map schema](references/codespec-map.schema.json)
- [Business Glossary schema](references/business-glossary.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples, JSON-oriented CLI workflows, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to read or update repository knowledge files and to run local relay-knowledge CLI diagnostics, indexing, query, status, and validation commands.]

## Skill Version(s):

1.1.18 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
