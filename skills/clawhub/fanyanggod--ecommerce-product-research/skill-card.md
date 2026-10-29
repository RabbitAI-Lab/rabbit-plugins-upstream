## Description:

Research ecommerce products and stores using TikTok and Facebook ads, product data, and store intelligence from PipiAds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fanyanggod](https://clawhub.ai/user/fanyanggod)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce researchers use this skill to investigate products, ads, advertisers, and stores across TikTok and Facebook using PipiAds data. It supports comparing pricing, landing pages, storefront patterns, and competitive density before running broad queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs a third-party npm MCP server that is external code and not bundled in the artifact for review.

Mitigation: Review the npm package before installation, keep the package pinned to the documented version, and install only in environments approved for third-party MCP servers.

Risk: The integration requires a PipiAds API key, and broad searches can consume account credits.

Mitigation: Use the least-exposed API key available, monitor credit usage, and collect category, price band, region, and platform before broad ecommerce queries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fanyanggod/skills/ecommerce-product-research)
- [PipiAds](https://www.pipiads.com)
- [PipiSpy](https://www.pipispy.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with setup commands, MCP tool suggestions, and ecommerce research summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend PipiAds MCP tool calls; API calls consume PipiAds account credits.]

## Skill Version(s):

1.0.1 (source: server release metadata, released 2026-04-02)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
