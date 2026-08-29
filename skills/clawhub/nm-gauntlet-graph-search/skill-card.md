## Description:

Searches the code knowledge graph by function, class, or type using FTS5 full-text search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to find code entities in a prebuilt local code graph and inspect matching symbols by name or qualified path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill expects to execute a local graph_query.py script from the associated plugin.

Mitigation: Install and use the skill only when the associated claude-night-market/gauntlet plugin is trusted.

Risk: Search results depend on the local .gauntlet/graph.db being present and current.

Mitigation: Build or refresh the graph database before relying on results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-gauntlet-graph-search)
- [gauntlet plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/gauntlet)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash commands and search-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns qualified names, file paths, line numbers, and relevance scores; requires an existing .gauntlet/graph.db.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
