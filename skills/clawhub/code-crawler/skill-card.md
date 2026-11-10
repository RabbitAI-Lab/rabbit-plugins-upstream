## Description:

Answer questions about code relationships in an indexed repository - callers, callees, impact, entry points, routes, DI wiring, dead code, cycles - using the code-crawler MCP server's SQLite property graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nithin554](https://clawhub.ai/user/nithin554)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to investigate how symbols connect in an indexed repository, including callers, callees, change impact, entry points, routes, dependency injection, reachability, and cycles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented `npx` commands use unpinned packages, so a later package resolution could introduce a compromised release.

Mitigation: Review the package and resolved version before installation, and use a pinned version when reproducibility is important.

Risk: Setup may propose edits to a client's configuration, and scanner coverage is partial.

Mitigation: Review the package and proposed configuration changes, approve edits deliberately, and inspect unresolved references when assessing the skill.

## Reference(s):

- [Edge semantics](reference/edge-semantics.md)
- [Tool reference](reference/tools.md)
- [Code Crawler homepage](https://nithin554.github.io/code-crawler/)
- [ClawHub skill page](https://clawhub.ai/nithin554/skills/code-crawler)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration]

**Output Format:** [Conversational text or Markdown, with code blocks when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Repository relationship findings and practical guidance; results depend on the indexed project and index freshness.]

## Skill Version(s):

0.1.81 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
