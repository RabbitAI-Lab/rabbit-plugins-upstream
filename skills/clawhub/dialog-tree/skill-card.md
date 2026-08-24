## Description:

Maintain a visual dialog tree: a local data file plus a self-contained HTML viewer in the project repo that maps branches of a long conversation as an interactive tree with resolve/delete marks and a built-up-to marker for incremental updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ikotelkin](https://clawhub.ai/user/ikotelkin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Claude Code users use this skill to maintain a navigable map of branching technical conversations, open questions, and resolved threads. It is most useful during long problem-solving sessions where context compaction or depth-first discussion can make unexplored branches hard to track.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tree node HTML is rendered in the local viewer, so untrusted or secret-bearing conversation data can create avoidable exposure or unsafe browser content.

Mitigation: Use trusted conversation data, escape code samples and special characters in node HTML, and avoid storing secrets or untrusted HTML in tree nodes.

Risk: Resolve/delete marks are stored in browser localStorage by treeId and origin, so changing tree IDs, file names, or serving origin can make user marks appear missing or collide with another tree.

Mitigation: Choose a unique stable treeId, keep paired HTML/data names consistent, and continue using the same file or localhost serving mode for an existing tree.

Risk: A static server used to view the tree could expose local project files beyond the intended user if bound too broadly.

Mitigation: Keep the static server for local use and serve only the directory that contains the tree files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ikotelkin/skills/dialog-tree)
- [Claude Code skills documentation](https://code.claude.com/docs/en/skills)
- [README](README.md)
- [Skill instructions](SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Project-local HTML and JavaScript files with Markdown-style guidance and shell/configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates a paired tree viewer and data file; browser state for resolve/delete marks is stored locally per treeId and origin.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
