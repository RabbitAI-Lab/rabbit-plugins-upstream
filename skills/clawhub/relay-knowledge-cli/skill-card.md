## Description: <br>
Relay Knowledge CLI guides agents to use the local relay-knowledge CLI for repository indexing, knowledge graph ingestion, GraphRAG queries, code graph search, feature flag analysis, impact analysis, and diagnostics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stevetdp](https://clawhub.ai/user/stevetdp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to help agents run relay-knowledge CLI workflows for local repository indexing, code and software graph queries, GraphRAG retrieval, feature flag analysis, impact analysis, setup diagnostics, and install or upgrade checks. It is intended for CLI-based repository knowledge work and explicitly keeps protocol integrations such as MCP and ACP out of scope. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Repository indexing may read private source code and store derived indexes in relay-knowledge runtime state. <br>
Mitigation: Use narrow repository paths, isolated temporary homes for tests, local deterministic backends where appropriate, and remove temporary runtime state after smoke checks. <br>
Risk: Running an untrusted or incompatible relay-knowledge binary could expose local repository content or produce misleading diagnostics. <br>
Mitigation: Prefer a bundled asset only after its version check succeeds, otherwise use a trusted published release or Cargo install path and verify release archives when downloading. <br>
Risk: Large indexing tasks can continue beyond command-runner timeouts and leave active leases or queued work. <br>
Mitigation: Inspect repo status, let managed services drain active work, wait for lease recovery when needed, and use bounded index-worker attempts for queued or retrying tasks. <br>


## Reference(s): <br>
- [Relay Knowledge GitHub Homepage](https://github.com/coolplayagent/relay-knowledge) <br>
- [ClawHub Skill Page](https://clawhub.ai/stevetdp/skills/relay-knowledge-cli) <br>
- [CLI Workflows](references/cli-workflows.md) <br>
- [Knowledge Map Workflows](references/knowledge-map-workflows.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Emphasizes machine-readable CLI output with --format json and status-driven handling for long-running local indexing tasks.] <br>

## Skill Version(s): <br>
1.1.13 (source: evidence release, skill metadata, target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
