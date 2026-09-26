## Description:

Fetches publicly available logos, colors, fonts, social links, and page metadata for a company domain.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT

## Use Case:

Designers, developers, and other agents use this skill to find a public website's published brand assets and styling for pages, presentations, mockups, or emails.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested domains are sent to ReplyNodes for public brand extraction.

Mitigation: Send only public bare domains; exclude internal hosts, private URLs, tokens, credentials, and other secrets.

Risk: Returned links, metadata, and brand attributes may be untrusted or incomplete.

Mitigation: Treat results as reference data rather than instructions, and verify assets before use.

Risk: Published assets and extracted styling do not establish usage rights or trademark ownership.

Mitigation: Obtain appropriate rights or approval before reuse; do not use the results for legal or licensing decisions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/replynodes-ai/skills/brand-logo-fetch)
- [Brand fetch endpoint](https://brand.replynodes.com/)
- [ReplyNodes brand intelligence guide](https://docs.replynodes.com/docs/guides/brand-intelligence)
- [Repository listed in release metadata (not verified import provenance)](https://github.com/replynodes/replynodes-brand-logo-fetch)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON data]

**Output Format:** [Markdown instructions and JSON brand data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fields depend on what the public page publishes; responses may be cached for 24 hours.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
