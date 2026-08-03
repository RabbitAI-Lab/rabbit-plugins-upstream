## Description: <br>
Relay Knowledge CLI guides agents to use the local relay-knowledge command for repository knowledge graph indexing, GraphRAG queries, code graph search, software relationship queries, feature flag lookup, impact analysis, and setup or upgrade diagnostics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stevetdp](https://clawhub.ai/user/stevetdp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to route repository understanding work through the local relay-knowledge CLI, including code graph lookup, software graph exploration, feature flag queries, impact analysis, and runtime diagnostics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Repository indexing and graph queries can create local indexes of selected code and runtime state. <br>
Mitigation: Use scoped paths, inspect existing repository aliases before registering new scopes, and set a temporary RELAY_KNOWLEDGE_HOME for tests when persistent state is not desired. <br>


## Reference(s): <br>
- [CLI Workflows](references/cli-workflows.md) <br>
- [Knowledge Map Workflows](references/knowledge-map-workflows.md) <br>
- [Relay Knowledge project homepage](https://github.com/coolplayagent/relay-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell command blocks and JSON-output preferences] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prefers scoped repository paths, machine-readable CLI output, and temporary RELAY_KNOWLEDGE_HOME values for isolated tests.] <br>

## Skill Version(s): <br>
1.1.13 (source: frontmatter metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
