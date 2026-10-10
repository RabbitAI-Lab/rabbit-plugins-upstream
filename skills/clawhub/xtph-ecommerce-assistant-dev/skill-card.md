## Description:

Helps ecommerce sellers connect a test shop, find 1688 products from images, and preview or publish sourced listings in the development environment.

This skill is for research and development only.

## Publisher:

[daiyangyang103240](https://clawhub.ai/user/daiyangyang103240)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and developers use this test-only assistant to authorize a shop, check shop status, find 1688 suppliers from product images, and preview or publish selected products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting a shop stores a local session token.

Mitigation: Use a test shop account, protect local session files, and never share the token in messages or logs.

Risk: Product images or image URLs are sent to the configured service for 1688 sourcing.

Mitigation: Submit only images you are comfortable sharing with the service.

Risk: Publishing can create shop listings, including automatically when explicitly requested.

Mitigation: Review the preview and selected products before confirming publication; request automatic publishing only when intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/daiyangyang103240/skills/xtph-ecommerce-assistant-dev)
- [Development shop application](https://puhuo-test.huitun.com)
- [Agent API protocol](references/api-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Conversational text and Markdown product tables with links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes sourcing results, preview or publication status, and links to continue in the test application.]

## Skill Version(s):

1.0.15 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
