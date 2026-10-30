## Description:

Find and verify work emails from a name and company — waterfall lookup across providers, one call for agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and outbound agents use this skill to find a person's professional email, verify an address before sending, or retrieve known email addresses for a company domain. It also supports list cleaning and lead enrichment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional MCP connection may expose a broader set of workspace tools than the email lookup capability suggests.

Mitigation: Check enabled tools and enforce an email-only allowlist before connecting; use the documented direct API calls if the MCP scope cannot be confirmed.

Risk: Lookup inputs are sent to Superagnt and its providers, and API use consumes credits.

Mitigation: Protect the API key, send only necessary lookup data, and review credit use.

Risk: The supplied shell examples have quoting and request-parameter gaps.

Mitigation: Correct shell quoting and supply complete endpoint request parameters before running the examples.

## Reference(s):

- [Email Finder documentation](https://superagnt.com/r/ch-email-finder-docs)
- [Email Finder API key](https://superagnt.com/r/ch-email-finder-key)
- [Email Finder MCP installation](https://www.superagnt.com/install?facet=email-finder)
- [Email Finder ClawHub listing](https://clawhub.ai/superagnt/skills/email-finder)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [JSON API responses and Markdown instructions with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns email lookup, verification, or domain email results with deliverability information when available.]

## Skill Version(s):

2.0.11 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
