## Description:

Answer questions about code relationships in an indexed repository - callers, callees, impact, entry points, routes, DI wiring, dead code, cycles - using the code-crawler MCP server's SQLite property graph. Use when the question is about how symbols connect (who calls this, what breaks if I change it, where does a request enter, is this reachable) rather than about text you can find by searching. Do not crawl a repository just to answer a question about a single file you already have open.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nithin554](https://clawhub.ai/user/nithin554)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to answer questions about how symbols connect across an indexed codebase, such as callers, call paths, routes, dependencies, and the impact of a change. It is best suited to questions about relationships across a repository rather than locating text in a single file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The separately downloaded code-crawler server and setup utilities may change independently of this skill release; the bundled evidence notes that the external software version is not fixed.

Mitigation: Use reviewed, fixed package versions and inspect client configuration changes before enabling the server.

Risk: Crawling a repository creates a saved SQLite index containing project-derived data.

Mitigation: Limit crawling to the intended repository and protect the saved index as project data.

## Reference(s):

- [Code Crawler project homepage](https://nithin554.github.io/code-crawler/)
- [ClawHub skill release](https://clawhub.ai/nithin554/skills/code-crawler)
- [Publisher profile](https://clawhub.ai/user/nithin554)
- [tools.md](artifact/reference/tools.md)
- [edge-semantics.md](artifact/reference/edge-semantics.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers are based on the indexed repository graph; relationship findings should be interpreted using edge confidence and external-target details.]

## Skill Version(s):

0.1.78 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
