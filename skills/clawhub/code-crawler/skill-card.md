## Description:

Answer questions about code relationships in an indexed repository using the code-crawler MCP server's SQLite property graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nithin554](https://clawhub.ai/user/nithin554)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to understand how symbols connect across an indexed codebase, including callers, callees, routes, dependency injection, and change impact. It helps answer structural questions that are harder to resolve with text search alone.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review rates the setup as suspicious because it uses unpinned npm packages and says some setup behavior is not fully disclosed; scanners did not establish malicious behavior, and coverage was partial because some referenced paths were unresolved.

Mitigation: Review the setup commands and generated configuration, pin package versions to reviewed releases, and check unresolved referenced paths before running or approving setup.

## Reference(s):

- [Code Crawler on ClawHub](https://clawhub.ai/nithin554/skills/code-crawler)
- [Code Crawler project homepage](https://nithin554.github.io/code-crawler/)
- [Tool reference](reference/tools.md)
- [Edge semantics reference](reference/edge-semantics.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands, Configuration, Code]

**Output Format:** [Markdown with prose, code snippets, and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Relationship results depend on the indexed project and index freshness.]

## Skill Version(s):

0.1.86 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
