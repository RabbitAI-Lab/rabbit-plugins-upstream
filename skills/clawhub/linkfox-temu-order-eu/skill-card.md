## Description:

Provides agent guidance and scripts for Temu EU order management through the LinkFox gateway, including order queries, shipping information, amounts, combined shipments, customization data, and verification uploads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and seller-operations teams use this skill to have an agent prepare and run LinkFox/Temu EU order API calls for order lists, details, shipping information, order amounts, combined shipments, customization data, and verification uploads.

### Deployment Geography for Use:

Europe (Temu EU order workflows)

## Known Risks and Mitigations:

Risk: The skill handles Temu access tokens, LinkFox API keys, seller order data, address data, customization data, and verification identifiers.

Mitigation: Use it only in trusted workspaces, keep API keys and access tokens out of chats and logs, and protect or rotate credentials stored under ~/.linkfox/temu-access-tokens.json.

Risk: Full API responses may be saved locally and small or inline responses may be printed to stdout.

Mitigation: Run the skill only where local saved responses are acceptable, review and secure generated linkfox data directories, and avoid inline output when responses may contain sensitive order or address data.

Risk: Generic proxy, non-EU site, onboarding, and payment-order helpers extend beyond the narrow EU order-query workflow.

Mitigation: Require explicit user confirmation before using generic proxy types, non-EU site options, onboarding flows, or payment order commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-order-eu)
- [API reference](references/api.md)
- [Partner EU order catalog](references/partner-eu-catalog.md)
- [Order API document index](references/apis/README.md)
- [Access token guidance](references/access-token.md)
- [Authorization and billing onboarding](references/onboarding.md)
- [Temu Partner EU documentation](https://partner-eu.temu.com/documentation?menu_code=dbd3d395963a408984b8ae7dbc5f64f9)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON files, API calls, guidance]

**Output Format:** [Markdown guidance, Python command snippets, JSON request and response data, and saved JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are written to a local linkfox session data directory; small responses may also print as JSON, while larger responses print summaries unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
