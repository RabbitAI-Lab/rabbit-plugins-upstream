## Description:

Evidence-first web and workspace search with bounded results, source labels, and machine-readable provenance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iyeque](https://clawhub.ai/user/iyeque)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can look up current web information or find relevant content in workspace memory and skills, with labeled search results for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Web queries may disclose sensitive information to Tavily when external search is enabled.

Mitigation: Use local-only search for private queries, and send queries to Tavily only when sharing them is acceptable.

Risk: Local results may expose snippets from workspace memory or skills, and web snippets may contain inaccurate claims.

Mitigation: Review who receives local results and verify important web claims against their original sources.

## Reference(s):

- [Unified Web Search on ClawHub](https://clawhub.ai/iyeque/skills/iyeque-unified-web-search)
- [iyeque publisher profile](https://clawhub.ai/user/iyeque)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON search results and warnings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bounded results include source labels, titles, scores, and snippets or content; web results may include URLs.]

## Skill Version(s):

1.3.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
