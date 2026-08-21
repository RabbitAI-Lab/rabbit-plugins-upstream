## Description:

Helps agents manage Shopee Bundle Deal promotions for authorized stores using LinkFox-provided scripts and reference material for the Shopee Open API Bundle Deal module.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers managing authorized Shopee stores use this skill to create, inspect, update, end, and delete Bundle Deal promotions and participating items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence marks the release suspicious and notes account login, API-key generation, purchase and payment QR-code flows, destructive store operations, and default full-response persistence.

Mitigation: Review the skill before installing, use it only with a trusted publisher and endpoint configuration, and confirm destructive actions such as ending or deleting promotions before running scripts.

Risk: Shopee and LinkFox responses may be stored in local linkfox session data, which can include operational store data.

Mitigation: Run the skill only in workspaces where local response persistence is acceptable, and review or remove saved response files according to local data-handling policy.

Risk: Endpoint override environment variables can redirect API traffic away from the default LinkFox endpoints.

Mitigation: Do not set endpoint override variables unless the destination is controlled and approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-bundle-deal)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [Shopee Bundle Deal API reference](https://open.shopee.com/documents/v2/v2.bundle_deal.add_bundle_deal?module=110&type=1)
- [Bundle Deal module overview](references/api.md)
- [Onboarding and authentication guidance](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON inputs or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full responses to local linkfox session data and summarize large responses unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
