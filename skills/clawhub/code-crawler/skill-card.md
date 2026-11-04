## Description:

Answers code relationship questions—such as callers, callees, impact, routes, dependency injection, reachability, and cycles—using an indexed repository graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nithin554](https://clawhub.ai/user/nithin554)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to answer questions about how symbols connect across a repository, including callers, execution paths, routes, dependency wiring, and change impact. It helps decide when a code graph is useful and cautions against crawling for simple file searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A repository crawl reads project files and saves an index that may contain sensitive project data.

Mitigation: Confirm the repository root and exclusions before crawling, and protect the saved index as project data.

Risk: The separately downloaded server implementation was unavailable for review, so its file access and network behavior were not verified.

Mitigation: Review and pin the package version before use, and approve project-scoped MCP configuration.

## Reference(s):

- [Code Crawler project homepage](https://nithin554.github.io/code-crawler/)
- [Code Crawler on ClawHub](https://clawhub.ai/nithin554/skills/code-crawler)
- [Edge semantics](reference/edge-semantics.md)
- [Tool reference](reference/tools.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance, Graph visualization text]

**Output Format:** [Markdown answers, optionally including Mermaid or Graphviz graph text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Graph findings should be interpreted with edge confidence and external-target semantics; list results may be paginated.]

## Skill Version(s):

0.1.77 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
