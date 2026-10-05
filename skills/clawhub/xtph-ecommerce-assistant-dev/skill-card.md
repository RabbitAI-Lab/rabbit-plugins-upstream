## Description:

Helps ecommerce sellers test shop authorization, 1688 image-based sourcing, product previews, and listing publication in a development environment.

This skill is for research and development only.

## Publisher:

[daiyangyang103240](https://clawhub.ai/user/daiyangyang103240)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and developers use this test-only assistant to connect a shop, check authorization, find 1688 products from an image, and preview or publish selected listings during development and verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An explicit direct-publish request can publish ready listings without a fresh item-by-item confirmation.

Mitigation: Prefer preview and confirmation; verify the selected products before requesting automatic publication.

Risk: Connecting the assistant grants access to a shop account in the test environment.

Mitigation: Connect only a development or test ecommerce account and review the requested shop before authorization.

Risk: Local session and preview workflow data may remain after use.

Mitigation: Periodically clear stored ~/.xtph session and workflow data when the skill is no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/daiyangyang103240/skills/xtph-ecommerce-assistant-dev)
- [Agent API protocol](references/api-protocol.md)
- [Test environment storefront](https://puhuo-test.huitun.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, HTML]

**Output Format:** [Chinese-language responses with product tables, preview summaries, publication results, and optional HTML product results page]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Displays up to 10 image-search results in source order; the optional HTML page is a manual link.]

## Skill Version(s):

1.0.14 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
