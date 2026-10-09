## Description:

Helps agents research questions and check citations against scholarly registries before presenting sourced conclusions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and agents use this skill to investigate questions, check bibliographies for fabricated or mismatched references, and prepare evidence-backed reports before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation checks may make outbound requests beyond the hosts named in the skill's security declaration.

Mitigation: Review network access before installation; use offline mode when external requests are inappropriate.

Risk: Optional external judge or NLI services may receive sensitive draft content.

Mitigation: Do not enable external judging for private drafts unless the endpoint is trusted; consider offline and no-cache modes for sensitive work.

Risk: MCP clients can supply reference URLs that trigger requests from the server host.

Mitigation: Expose the MCP server only to trusted clients and review its network access.

## Reference(s):

- [Cite Holmes ClawHub release](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Verification details](artifact/references/verification-details.md)
- [Medical evidence mode](artifact/references/medical-mode.md)
- [MCP integration guide](artifact/mcp/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Bibliography files, Guidance]

**Output Format:** [Research reports and citation-verification results in Markdown or JSON; bibliography exports in BibTeX, RIS, CSV, or GB/T 7714-2025 text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-reference verdicts and evidence grades; unverified citations remain labeled for review.]

## Skill Version(s):

3.10.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
