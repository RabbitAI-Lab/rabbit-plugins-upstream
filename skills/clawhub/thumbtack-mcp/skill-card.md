## Description:

Find local Thumbtack service professionals by trade and ZIP code, and read public profiles with ratings, reviews, credentials, hours, and pricing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can look up local service professionals and summarize public Thumbtack profiles without signing in or contacting a professional.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookups send anonymous requests to Thumbtack and process returned pages locally.

Mitigation: Use only if outbound requests are acceptable, and limit profile URLs to genuine Thumbtack pages.

Risk: Account messages, quotes, projects, and other logged-in content are outside the read-only lookup scope.

Mitigation: Do not use this skill for account actions or logged-in Thumbtack pages.

## Reference(s):

- [Thumbtack lookup recipes](references/discovery.md)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/thumbtack-mcp)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell examples and structured profile summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public search and profile information; prices and other fields may be absent.]

## Skill Version(s):

1.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
