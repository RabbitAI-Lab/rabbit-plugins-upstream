## Description:

Creates GPS-anchored BillboardBug business deals and optional social posts, then verifies publication through read-back.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bgaut007](https://clawhub.ai/user/bgaut007)

### License/Terms of Use:

MIT-0

## Use Case:

Business operators and their agents use this skill to publish location-based promotions and related social posts under an authorized BillboardBug account, then check the published content and record a receipt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key authorizes publishing under the account owner's identity.

Mitigation: Install only if the account owner trusts BillboardBug; keep the key in its environment variable and review each deal or post before approving publication.

Risk: Published billboards and posts may remain publicly visible, and media prompts or captions may reveal confidential information.

Mitigation: Exclude confidential information from prompts and captions; confirm the publication window and disable or delete content when it should no longer be visible.

Risk: Featured placement can incur charges.

Mitigation: Keep featured placement off unless the account owner explicitly approves the paid option.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bgaut007/skills/billboardbug-deal-creator)
- [BillboardBug public API documentation](https://east-us-api.billboardbug.com/public-api/docs)
- [BillboardBug OpenAPI specification](https://east-us-api.billboardbug.com/public-api/spec)
- [BillboardBug website](https://billboardbug.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a publication receipt with deal and post IDs, read-back status, and reported gaps.]

## Skill Version(s):

1.1.2 (source: skill frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
