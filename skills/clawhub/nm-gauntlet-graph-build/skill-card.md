## Description:

Builds or updates the code knowledge graph via tree-sitter AST and SQLite.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use graph-build to build or refresh a local source-code graph before codebase search, blast-radius analysis, or flow tracing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill indexes source structure from the selected directory into .gauntlet/graph.db.

Mitigation: Run it only in the intended repository and review handling of the generated .gauntlet/graph.db file; the skill creates .gauntlet/.gitignore to help prevent accidental commits.

Risk: The related full plugin experience includes additional agents, hooks, and commands outside this skill text.

Mitigation: Review the full plugin separately before installing or enabling those additional components.

## Reference(s):

- [graph-build on ClawHub](https://clawhub.ai/athola/skills/nm-gauntlet-graph-build)
- [claude-night-market gauntlet plugin](https://github.com/athola/claude-night-market/tree/master/plugins/gauntlet)

## Skill Output:

**Output Type(s):** [shell commands, markdown, guidance]

**Output Format:** [Markdown with bash commands and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update .gauntlet/graph.db and .gauntlet/.gitignore in the selected codebase.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter states 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
