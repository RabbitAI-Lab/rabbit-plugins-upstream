## Description:

thumbtack-mcp helps agents query public Thumbtack search and pro profile pages from a shell, returning service provider details such as ratings, reviews, credentials, business hours, and pricing without requiring an API key or login.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use this skill to search public Thumbtack listings by trade and ZIP code, inspect pro profiles, and compose repeatable curl, jq, and Node.js extraction workflows for local service provider research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes anonymous requests to Thumbtack from the user's machine, which may have terms-of-use or scraping-policy implications.

Mitigation: Use only public HTTPS Thumbtack URLs, avoid credentials or private account data, and review Thumbtack's terms before relying on automated scraping.

Risk: Thumbtack page structures, redirects, and GraphQL responses can vary or change, causing missing fields or misleading extraction results.

Mitigation: Resolve canonical service slugs, choose the extractor mode that matches the page type, branch on optional or union fields, and check GraphQL errors before using returned data.

## Reference(s):

- [Thumbtack discovery recipes](artifact/references/discovery.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/thumbtack-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, jq filters, and JSON extraction guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are read-only lookup and parsing instructions for public Thumbtack pages; profile and search page shapes may vary by category.]

## Skill Version(s):

0.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
