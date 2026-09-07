## Description:

Uses Amazon product details and review evidence to diagnose buyer decision barriers and suggest conversion-focused listing copy improvements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon marketplace operators and ecommerce teams use this skill to turn collected ARI product and review evidence into listing conversion diagnostics and copy recommendations. It is not intended for sales or conversion-rate prediction, ad bidding, or automatic publication of Amazon listing changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits through paid collection, analysis, or operations flows.

Mitigation: Use quote-only phrasing for pricing checks, require explicit approval before paid operations, and disable or lower auto-confirm settings when every charge needs review.

Risk: The skill stores and uses an ARI API key for account access.

Mitigation: Authorize through the browser or local configuration, never paste API keys into chat or reports, and revoke or recreate the key from the ARI user center if exposure is suspected.

Risk: The skill can change ongoing monitoring schedules or confirmation settings.

Mitigation: Review proposed schedule and auto-confirm changes before approval, and verify account settings after any requested management action.

Risk: The security review notes broader advertising and operations features than the conversion-copy description suggests.

Mitigation: Limit use to the intended listing conversion workflow unless the user explicitly requests a broader ARI operation, and review recommendations before applying them to listings or campaigns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/conversion-copy)
- [ARI CLI and API reference](artifact/references/reference.md)
- [Amazon conversion workflow reference](artifact/references/operation-workflow.md)
- [ARI Amazon review assistant usage guide](artifact/使用说明.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text guidance, with shell command snippets and service-returned JSON details when needed for setup, quoting, or troubleshooting.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include review-evidence summaries, conversion-copy recommendations, ARI report links, credit usage, balance information, and account or monitoring status returned by the service.]

## Skill Version(s):

1.4.7 (source: frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
