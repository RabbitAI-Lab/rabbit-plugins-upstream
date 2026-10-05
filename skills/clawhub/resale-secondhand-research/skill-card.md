## Description:

Researches public secondhand, resale, and handmade listings, sellers, and prices across nine marketplaces through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers, resellers, and researchers use this skill to find and compare public listings, inspect shops and sellers, and check resale prices across supported marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace searches and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only when that disclosure is acceptable; keep the key in the environment and never commit it.

Risk: Unnecessary marketplace or route requests may consume API credits.

Mitigation: Limit requests to the marketplaces and routes the user asked for.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/resale-secondhand-research)
- [Supported API endpoints](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [JSON from marketplace queries; Markdown or plain-text research summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public listing, seller, and pricing results; API requests may consume Crawlora credits.]

## Skill Version(s):

1.0.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
