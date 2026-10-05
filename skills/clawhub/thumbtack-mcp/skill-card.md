## Description:

Helps agents search Thumbtack for local service professionals and read public profiles, reviews, credentials, hours, and pricing from the shell without an account or MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to find local service professionals by trade and ZIP code and compare publicly available profile details. It does not access accounts, book services, or contact professionals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Anonymous lookups send requests from the user's shell to Thumbtack.

Mitigation: Install only if these network requests are acceptable, and keep supplied URLs on Thumbtack domains.

Risk: Search inputs could disclose private information, and heavy use could conflict with site terms or rate limits.

Mitigation: Do not include private data in requests; review Thumbtack's terms and limit request volume.

## Reference(s):

- [Thumbtack discovery recipes](references/discovery.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON]

**Output Format:** [Markdown guidance, shell commands, and structured search or profile results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public information; results, availability, and pricing may vary.]

## Skill Version(s):

1.1.5 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
