## Description:

Answer questions about code relationships in an indexed repository - callers, callees, impact, entry points, routes, DI wiring, dead code, cycles - using the code-crawler MCP server's SQLite property graph. Use when the question is about how symbols connect (who calls this, what breaks if I change it, where does a request enter, is this reachable) rather than about text you can find by searching. Do not crawl a repository just to answer a question about a single file you already have open.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nithin554](https://clawhub.ai/user/nithin554)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to understand how symbols in an indexed codebase connect, assess change impact, trace execution paths, and inspect framework wiring. It helps answer relationship questions that are difficult to resolve with text search alone.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The index can contain details about private source code.

Mitigation: Choose the repository to index deliberately and protect its SQLite index database.

Risk: Registering the third-party server can change client configuration, and the downloaded server and its dependencies were not audited in the supplied security review.

Mitigation: Review client configuration changes and use reviewed, pinned package versions.

Risk: Graph results can be incomplete or misleading when the index is stale or relationships rely on dynamic dispatch, frameworks, or reflection.

Mitigation: Check index status before relying on negative results and use the documented confidence, external-target, and reflection guidance when interpreting findings.

## Reference(s):

- [Code Crawler homepage](https://nithin554.github.io/code-crawler/)
- [ClawHub release page](https://clawhub.ai/nithin554/skills/code-crawler)
- [Tool reference](artifact/reference/tools.md)
- [Edge semantics](artifact/reference/edge-semantics.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Natural language text, optionally structured as Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers are based on the indexed graph; confidence bands, external targets, and unresolved or framework-driven relationships affect interpretation.]

## Skill Version(s):

0.1.76 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
