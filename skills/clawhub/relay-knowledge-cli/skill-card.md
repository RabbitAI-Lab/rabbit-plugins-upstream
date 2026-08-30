## Description:

Relay Knowledge CLI guides agents through local repository knowledge-map governance, code graph indexing, GraphRAG queries, diagnostics, and commit-driven update loops using the relay-knowledge command line.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stevetdp](https://clawhub.ai/user/stevetdp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to bootstrap and validate repository knowledge maps, query indexed code and business knowledge, and keep context current after commits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to index repository contents and maintain local knowledge-map or runtime state, which may expose sensitive private-code context if used too broadly.

Mitigation: Install only from trusted published relay-knowledge channels, review before service installation or broad repository indexing, and scope indexing to repositories and paths the user authorizes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/stevetdp/skills/relay-knowledge-cli)
- [Relay Knowledge Homepage](https://github.com/coolplayagent/relay-knowledge)
- [Relay Knowledge CLI Workflows](references/cli-workflows.md)
- [Knowledge Map and Code Map Workflows](references/knowledge-map-workflows.md)
- [Relay Knowledge Map v3 Artifacts Schema](references/knowledge-map.schema.json)
- [Relay CodeSpec Map v3 Root Schema](references/codespec-map.schema.json)
- [Relay Knowledge Business Glossary v1 Schema](references/business-glossary.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON-oriented CLI workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides local CLI execution and interpretation of repository indexing, status, query, diagnostics, and map validation outputs.]

## Skill Version(s):

1.1.16 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
