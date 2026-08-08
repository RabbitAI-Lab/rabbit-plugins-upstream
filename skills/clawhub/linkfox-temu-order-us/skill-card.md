## Description:

This skill helps agents manage Temu US orders through LinkFox, including order lookup, details, shipping information, amounts, combined shipments, customization data, and SN/IMEI verification uploads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to query and manage Temu US order workflows through LinkFox, including order discovery, shipping data retrieval, reconciliation details, combined shipment checks, customization data, and verification uploads.

### Deployment Geography for Use:

United States for Temu US marketplace workflows; otherwise Global where LinkFox, Temu, and local data handling requirements permit use.

## Known Risks and Mitigations:

Risk: The skill routes Temu order and customer data through LinkFox.

Mitigation: Use it only when LinkFox handling of Temu order and customer data is intended and approved for the account.

Risk: The security summary identifies plaintext local storage of Temu tokens and full API responses.

Mitigation: Run in a trusted workspace, restrict file access, and remove stored tokens or response files when they are no longer needed.

Risk: Gateway and login endpoint override environment variables can redirect traffic if set incorrectly.

Mitigation: Avoid endpoint overrides unless they point to trusted LinkFox infrastructure.

Risk: Generic proxy behavior can grant broader API access than order-only workflows require.

Mitigation: Prefer the order-specific scripts and use the generic proxy only when broader authority is intended.

Risk: Onboarding and payment-related commands may affect account setup or billing.

Mitigation: Treat onboarding and payment actions as explicit user-approved steps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-order-us)
- [API reference](references/api.md)
- [Temu accessToken authorization](references/access-token.md)
- [Partner US catalog](references/partner-us-catalog.md)
- [Order API documents](references/apis/README.md)
- [Temu Partner US documentation](https://partner-us.temu.com/documentation)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples, shell commands, and references to Python scripts that may write JSON response files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts are documented to save complete API responses under a workspace linkfox data directory and print either full JSON or summaries depending on response size.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
