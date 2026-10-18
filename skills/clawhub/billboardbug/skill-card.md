## Description:

Guides agents through creating GPS-anchored BillboardBug deals and social posts, then verifying them with read-back receipts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bgaut007](https://clawhub.ai/user/bgaut007)

### License/Terms of Use:

MIT-0

## Use Case:

Business operators and their authorized agents use this skill to publish location-based deals and chirps through BillboardBug, confirm the published content, and report a receipt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can publish or change public deals and chirps under the account holder's identity.

Mitigation: Confirm the business and exact content with the account holder, and review each create, update, or delete action before execution.

Risk: Exposure of the BillboardBug API key could allow unauthorized account activity.

Mitigation: Keep the key in the BILLBOARDBUG_API_KEY environment variable; do not include it in chat, posts, files, or logs.

Risk: Featured placement may incur charges, and deals have no built-in end-date field in the described workflow.

Mitigation: Require explicit approval for paid featured placement; record the promotion end date and disable the deal when it ends.

Risk: Receipt wording may imply a direct deal-to-chirp link that the post does not contain.

Mitigation: Report verified deal and chirp IDs separately, and clearly note that the post has no deal ID field.

## Reference(s):

- [BillboardBug skill listing](https://clawhub.ai/bgaut007/skills/billboardbug)
- [BillboardBug homepage](https://billboardbug.com)
- [BillboardBug app and API key settings](https://app.billboardbug.com)
- [BillboardBug API documentation](https://east-us-api.billboardbug.com/public-api/docs)
- [BillboardBug OpenAPI specification](https://east-us-api.billboardbug.com/public-api/spec)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash code blocks and a receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Receipt records deal and chirp IDs, read-back status, and any gaps or errors.]

## Skill Version(s):

1.2.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
