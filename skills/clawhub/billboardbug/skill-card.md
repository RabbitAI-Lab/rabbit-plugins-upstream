## Description:

Creates location-anchored BillboardBug deals and social chirps, then verifies published content by reading it back.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bgaut007](https://clawhub.ai/user/bgaut007)

### License/Terms of Use:

MIT-0

## Use Case:

Business owners and their authorized agents use this skill to publish location-based promotions and social posts through BillboardBug, with confirmation and read-back receipts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public deals or chirps could include unverified claims or sensitive business details.

Mitigation: Confirm the business and offer details, and review each publishing summary before approval.

Risk: The account API key authorizes publishing under the operator's account.

Mitigation: Keep the key in the environment; do not include it in posts, logs, or receipts.

Risk: Promotions may remain visible past their end date, and featured placement may incur charges.

Mitigation: Record the end date and disable expired deals; require explicit approval before enabling paid featured placement.

## Reference(s):

- [BillboardBug skill release](https://clawhub.ai/bgaut007/skills/billboardbug)
- [BillboardBug](https://billboardbug.com)
- [BillboardBug public API documentation](https://east-us-api.billboardbug.com/public-api/docs)
- [BillboardBug OpenAPI specification](https://east-us-api.billboardbug.com/public-api/spec)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown summaries and receipts, with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-back receipts include published deal and chirp identifiers and any errors.]

## Skill Version(s):

1.2.2 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
