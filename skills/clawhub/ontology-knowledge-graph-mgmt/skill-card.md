## Description: <br>
Guides agents through knowledge graph completion, synchronization, repair, and search workflows, including graph.jsonl validation, SQLite sync, vector search integration, and optional vector database setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[william202404](https://clawhub.ai/user/william202404) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to maintain ontology-backed knowledge graphs by validating graph.jsonl records, adding entities and relationships, syncing data to SQLite, indexing content for vector search, and checking end-to-end search behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can run local scripts, update graph data, configure vector database backends, and schedule recurring index updates. <br>
Mitigation: Review proposed commands before execution, back up graph and SQLite data before changes, use least-privilege service credentials for any vector database integration, and require confirmation before production updates. <br>
Risk: The artifact declares that graph_sync.py, graph_vectorize.py, and graph_search.py are external dependencies not included with the skill. <br>
Mitigation: Obtain these utilities from a trusted project repository or implement them against the documented interfaces, then scan and test them before relying on the workflow. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline JSON examples, bash commands, and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill references external Python graph utilities that are not bundled in the artifact.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
