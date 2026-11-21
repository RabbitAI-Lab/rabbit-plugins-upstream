## Description:

Analyze source-code projects through a pre-built local code graph for symbol source, call paths, callers and callees, change impact, affected tests, and file inventory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wei840222](https://clawhub.ai/user/wei840222)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use codegraph to answer codebase questions from a local code graph, including symbol lookup, call relationships, change impact, affected tests, and project file inventory. It is most useful when a project is already indexed and the agent needs graph-backed source context before answering or editing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented installation path can execute mutable remote code or install an unpinned global package.

Mitigation: Use a pinned, verified release and avoid curl-pipe-shell or unpinned global npm installation paths unless they have been reviewed.

Risk: The third-party CLI indexes local repositories and may change the user's environment through agent wiring, upgrades, daemon behavior, or telemetry.

Mitigation: Authorize only the specific actions needed, review telemetry and daemon behavior before use, and do not enable agent wiring or upgrades by default.

Risk: Index-changing commands modify the local .codegraph directory, and uninit removes it.

Mitigation: Run init, index, sync, unlock, or uninit only after explicit user authorization; fall back to built-in file reading and search when authorization is absent.

## Reference(s):

- [CodeGraph CLI Reference](references/cli-reference.md)
- [codegraph ClawHub Skill Page](https://clawhub.ai/wei840222/skills/codegraph)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown prose with path anchors, source snippets, and inline shell commands when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include verbatim source excerpts from the local code graph; index-changing commands require explicit authorization.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
