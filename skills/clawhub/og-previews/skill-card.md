## Description:

Checks social link previews and guides fixes to Open Graph and Twitter card metadata and images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[egorshar](https://clawhub.ai/user/egorshar)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site owners use this skill to check how pages appear when shared, repair social metadata, and install branded preview images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checking a page shares its URL with getwowlink, which may disclose private or unpublished pages.

Mitigation: Use only URLs approved for third-party checking; avoid private, internal, embargoed, or secret URLs.

Risk: Replacing social image tags may change existing site previews incorrectly.

Mitigation: Review code edits before deployment, replace rather than duplicate og:image tags, and verify live previews afterward.

## Reference(s):

- [getwowlink link-preview checker](https://www.getwowlink.com/og-checker)
- [getwowlink MCP server](https://mcp.getwowlink.com)
- [getwowlink preview design](https://www.getwowlink.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration guidance]

**Output Format:** [Markdown with HTML meta tag examples and preview report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preview reports come from getwowlink; the site owner publishes designs and deploys code changes.]

## Skill Version(s):

1.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
