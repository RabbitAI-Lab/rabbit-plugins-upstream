## Description:

Answer questions about code relationships in an indexed repository - callers, callees, impact, entry points, routes, DI wiring, dead code, cycles - using the code-crawler MCP server's SQLite property graph. Use when the question is about how symbols connect (who calls this, what breaks if I change it, where does a request enter, is this reachable) rather than about text you can find by searching. Do not crawl a repository just to answer a question about a single file you already have open.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nithin554](https://clawhub.ai/user/nithin554)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use the skill to answer structural questions about an indexed codebase, such as which code calls a symbol, what a change may affect, and how routes or dependencies are wired. It helps decide when to use graph analysis and when ordinary text search or reading a file is a better fit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the package or enabling generated MCP configuration can introduce unexpected code or settings; the security scan was partial and its evidence is incomplete.

Mitigation: Use reviewed, pinned package versions and inspect generated configuration before enabling it.

## Reference(s):

- [Code Crawler project homepage](https://nithin554.github.io/code-crawler/)
- [Code Crawler ClawHub release page](https://clawhub.ai/nithin554/skills/code-crawler)
- [Tool reference](artifact/reference/tools.md)
- [Edge semantics reference](artifact/reference/edge-semantics.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Text or Markdown; graph exports as Mermaid or Graphviz text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers depend on the indexed repository and may include confidence and coverage caveats.]

## Skill Version(s):

0.1.85 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
