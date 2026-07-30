## Description: <br>
Builds or updates the code knowledge graph via tree-sitter AST and SQLite. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to build or refresh a repository-local code knowledge graph before code search, blast-radius analysis, flow tracing, or structural review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill parses the selected codebase and stores a local structural index in `.gauntlet/graph.db`. <br>
Mitigation: Run it from the intended repository, or provide a specific target path, to avoid indexing more code than intended. <br>
Risk: The generated graph database is repository-local state. <br>
Mitigation: Keep `.gauntlet/.gitignore` in place so the SQLite graph is not accidentally committed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-gauntlet-graph-build) <br>
- [Gauntlet plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/gauntlet) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May report files parsed, nodes created, edges created, and duration after building or updating the graph.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
