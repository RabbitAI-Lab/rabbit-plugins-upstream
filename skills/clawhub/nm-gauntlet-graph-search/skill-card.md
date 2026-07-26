## Description: <br>
Searches the code knowledge graph by function, class, or type using FTS5 full-text search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to find functions, classes, and types in a prebuilt Gauntlet code knowledge graph, then inspect matching source locations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs a local Python query command in the agent workspace. <br>
Mitigation: Review the command before execution and run it only in the intended workspace with the expected .gauntlet/graph.db file. <br>
Risk: Search results depend on a prebuilt graph database and may be stale or incomplete. <br>
Mitigation: Build or refresh the graph before relying on results, and inspect source files before making code changes. <br>


## Reference(s): <br>
- [Gauntlet plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/gauntlet) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with shell command examples and text search results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results include qualified names, file paths, line numbers, and relevance scores when the graph query succeeds.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
