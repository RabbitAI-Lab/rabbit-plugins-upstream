## Description:

Find domain names that are actually registrable. Calls Domain Search King's remote MCP (live RDAP). Never guess availability. No API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnsmalls22-rgb](https://clawhub.ai/user/johnsmalls22-rgb)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and naming workflows use this skill to find and check domain names through Domain Search King's live RDAP-backed service without guessing availability. It helps agents return available names, pattern-based domain sweeps, due-diligence details, and registration links for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential product names, acquisition targets, unreleased brands, or other sensitive naming ideas may be sent to Domain Search King's external service for lookup.

Mitigation: Use nonsensitive descriptors or obtain appropriate approval before checking confidential names with the external service.

Risk: Returned registration links are external links, and domain availability does not establish trademark clearance.

Mitigation: Perform registrar, ownership, and trademark due diligence before buying or recommending a domain.

Risk: The external service may fail, return empty results, or be constrained by fair-use limits.

Mitigation: Report failed or empty lookups plainly and do not substitute guessed domain availability.

## Reference(s):

- [Domain Search King MCP documentation](https://domainsearchking.com/mcp)
- [Domain Search King MCP endpoint](https://domainsearchking.com/api/mcp)
- [Domain Search King AI hallucination index](https://domainsearchking.com/ai-hallucination-index)
- [ClawHub skill listing](https://clawhub.ai/johnsmalls22-rgb/skills/dsk-available-domains)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with domain availability results, register URLs, due-diligence notes, and optional curl or MCP configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on Domain Search King's external service and live registry data; the skill instructs agents not to guess availability or complete purchases.]

## Skill Version(s):

1.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
