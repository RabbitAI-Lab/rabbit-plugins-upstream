## Description: <br>
Builds or updates a local code knowledge graph for a repository using tree-sitter AST parsing and SQLite. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to build or refresh a repository code graph before codebase search, blast-radius analysis, or flow tracing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill scans the selected directory and writes local graph files under .gauntlet/. <br>
Mitigation: Run it only on repositories intended for indexing, confirm the target path before execution, and review generated .gauntlet files before relying on them. <br>


## Reference(s): <br>
- [Gauntlet plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/gauntlet) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update .gauntlet/graph.db and .gauntlet/.gitignore in the selected repository.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
