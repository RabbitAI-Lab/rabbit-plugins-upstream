## Description: <br>
Searches the code knowledge graph by function, class, or type using FTS5 full-text search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to search an existing Gauntlet code graph for functions, classes, or types and inspect matching qualified names, file paths, line numbers, and relevance scores. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs a referenced local query script. <br>
Mitigation: Install it only when the Gauntlet plugin script is present and trusted. <br>
Risk: Search results may expose local code names, paths, and line numbers to the active agent session. <br>
Mitigation: Use it only in agent sessions authorized to inspect the target repository. <br>


## Reference(s): <br>
- [Gauntlet plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/gauntlet) <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-gauntlet-graph-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with shell command examples and search result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an existing .gauntlet/graph.db and a trusted Gauntlet graph_query.py script available through CLAUDE_PLUGIN_ROOT.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence; artifact frontmatter shows 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
