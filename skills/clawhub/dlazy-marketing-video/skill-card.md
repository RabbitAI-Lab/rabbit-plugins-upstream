## Description:

Creates promotional and ecommerce videos from product details, listings, or a marketing brief using the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers and merchants use this skill to create product ads and social-media marketing videos from briefs, product documents, or ecommerce listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to the third-party dLazy service.

Mitigation: Share only content approved for third-party processing and review attachments before upload.

Risk: The CLI may store an API key locally, and continuing a project may reuse earlier context.

Mitigation: Protect or revoke the API key as needed and check the project before continuing a session.

Risk: Installing a third-party CLI introduces package-supply-chain exposure.

Mitigation: Review the package and linked source before installation; use the pinned on-demand npx option if a persistent global install is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-marketing-video)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streaming text with generated-video links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-based follow-up conversations can reuse prior context.]

## Skill Version(s):

1.0.19 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
