## Description:

Guides an agent to use the 店雷达 dld MCP connector for 1688 product research, hot-product discovery, supplier assessment, product sales analysis, category browsing, and visual result presentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[b18797245781-commits](https://clawhub.ai/user/b18797245781-commits)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an assistant through 1688 product-selection workflows, including product search, ranking queries, single-product trend analysis, category lookup, supplier evaluation, and presentation of image-rich product results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend 店雷达 connector points, including for the initial account and connector availability check.

Mitigation: Install and use it only when the user specifically wants 店雷达-backed 1688 product research, and make point consumption clear before repeated connector calls.

Risk: Product-selection guidance may depend on connector availability, authorization, and returned marketplace data.

Mitigation: Check connector status first, stop on configuration or authorization failure, and treat returned data as decision support rather than a guaranteed purchasing recommendation.

## Reference(s):

- [店雷达 MCP registration](https://www.dianleida.net/mcp)
- [店雷达 MCP configuration documentation](https://www.dianleida.net/mcp/docs/)
- [1688 product-selection MCP API reference](references/api_reference.md)
- [1688 product-selection domain knowledge](references/domain_knowledge.md)
- [ClawHub skill page](https://clawhub.ai/b18797245781-commits/skills/dld-skills)
- [Publisher profile](https://clawhub.ai/user/b18797245781-commits)

## Skill Output:

**Output Type(s):** [guidance, API Calls, markdown, code, configuration]

**Output Format:** [Markdown guidance with structured tables, product images, product links, optional rendered HTML cards, and MCP tool-call parameter guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to check connector availability before tool use and to present concise product analysis with next-step recommendations.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
