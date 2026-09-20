## Description:

Query thumbtack.com from a shell to search local service pros by trade and zip, and read pro profiles with ratings, reviews, credentials, business hours, and pricing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to compose shell commands that retrieve public Thumbtack search and profile data without an MCP server, login, API key, or browser extension. It is useful for one-shot lookups or scripts that compare local service providers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes anonymous outbound requests to Thumbtack from the shell.

Mitigation: Use only public https://www.thumbtack.com/ pages, avoid credentials or private account data, and review requests for compliance with Thumbtack terms and rate limits.

Risk: Thumbtack page structures, GraphQL fields, or category-specific data shapes may change and cause incomplete or misleading parsed output.

Mitigation: Check command errors and JSON fields before relying on results, follow redirects to canonical slugs, branch on union types such as priceInfo, and verify important provider details on Thumbtack.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/thumbtack-mcp)
- [Thumbtack discovery recipes](references/discovery.md)
- [Thumbtack](https://www.thumbtack.com)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline shell, jq, and JavaScript examples that produce JSON from Thumbtack pages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are read-only lookup recipes; the bundled extractor reads HTML from stdin and writes parsed JSON to stdout.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
