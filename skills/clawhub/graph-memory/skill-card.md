## Description: <br>
Query the agent's knowledge graph for entities, relationships, and statistics. Enables natural language exploration of accumulated session memory without shell commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to query persistent OpenClaw graph memory for entities, relationships, and graph-wide statistics from prior sessions. It supports context lookup for past people, projects, tools, concepts, files, errors, topics, institutions, and research papers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can surface sensitive prior-session memory about people, files, projects, and errors. <br>
Mitigation: Install it only in workspaces where access to accumulated graph memory is intended, and review results before sharing them outside that workspace. <br>
Risk: Graph memory may be incomplete or vary in extraction quality because not all sessions are processed. <br>
Mitigation: Treat returned entities, relationships, and statistics as contextual leads that require verification against source materials before important decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/space-cadet/skills/graph-memory) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown strings returned by graph_search, graph_stats, and graph_related.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include entity names, types, mention counts, relationship paths, graph statistics, and error messages from the local graph memory database.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
