## Description:

Creates location-based BillboardBug deals and social chirps, then verifies publication with read-back.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bgaut007](https://clawhub.ai/user/bgaut007)

### License/Terms of Use:

MIT-0

## Use Case:

Business owners and authorized agents use this skill to publish location-based promotions and social posts under the owner's BillboardBug account, then check that they are live.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can publish and manage public deals and chirps under the account owner's identity.

Mitigation: Review the create, update, or delete summary and require explicit approval before account changes.

Risk: Exposure of the BillboardBug API key could enable unauthorized account actions.

Mitigation: Keep the key in the environment; never include it in chat, posts, files, or logs.

Risk: Business details in generated-image prompts or chirps may become public.

Mitigation: Avoid confidential details and confirm promotional claims and locations before posting.

## Reference(s):

- [BillboardBug skill listing](https://clawhub.ai/bgaut007/skills/billboardbug-deal-creator)
- [BillboardBug homepage](https://billboardbug.com)
- [BillboardBug API documentation](https://east-us-api.billboardbug.com/public-api/docs)
- [BillboardBug OpenAPI specification](https://east-us-api.billboardbug.com/public-api/spec)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and a publication receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Receipts include deal and chirp IDs, read-back results, and any errors.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
