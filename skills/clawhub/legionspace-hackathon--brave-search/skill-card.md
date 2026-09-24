## Description:

Web search and content extraction via Brave Search API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search the web, find documentation or current facts, and extract readable page content without an interactive browser.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can fetch arbitrary web pages from the agent environment, which may expose private network locations or metadata services if used with untrusted URLs.

Mitigation: Run it only with public URLs and block network egress to private networks and metadata services.

Risk: Search queries and fetched page URLs may contain sensitive information.

Mitigation: Do not use confidential queries, internal links, regulated data, or customer data with this skill.

Risk: The documented Brave API key requirement does not match the script behavior, which fetches Brave Search HTML directly.

Mitigation: Confirm the intended Brave integration and update documentation or implementation before relying on API-key controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/brave-search)
- [Publisher profile](https://clawhub.ai/user/legionspace-hackathon)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Plain text search results with optional markdown page content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search output includes title, link, snippet, and optional extracted content capped by the script.]

## Skill Version(s):

1.0.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
