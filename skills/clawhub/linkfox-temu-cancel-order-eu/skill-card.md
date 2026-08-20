## Description:

Helps agents operate Temu Europe order-cancellation workflows through LinkFox, including buyer cancellation review, seller cancellation appeals, out-of-stock cancellation requests, result checks, token setup, and signed file downloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and developer agents use this skill to prepare and run Temu EU buyer and seller cancellation tasks through LinkFox with the required LinkFox and Temu credentials.

### Deployment Geography for Use:

Europe / EMEA for Temu EU marketplace workflows

## Known Risks and Mitigations:

Risk: The skill can initiate live Temu EU cancellation and appeal actions through LinkFox.

Mitigation: Review order identifiers, cancellation type, and request payloads before running any script that submits a cancellation or appeal.

Risk: The skill uses LinkFox API keys and Temu access tokens, and can store Temu tokens locally for reuse.

Mitigation: Use scoped credentials where possible, avoid placing long-lived tokens in shell history, and remove saved token-store entries that are no longer needed.

Risk: Full API responses are persisted locally and may contain commerce or customer order data.

Mitigation: Periodically delete saved response files and avoid sharing the local linkfox data directory.

Risk: Onboarding commands may involve account registration, billing checks, or payment flows.

Mitigation: Treat onboarding and payment commands as separate account-management actions and run them only after explicit user confirmation.

Risk: Signed file download support can retrieve files through the LinkFox gateway.

Mitigation: Download only expected Temu signed resources and inspect downloaded content before using it in downstream workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-cancel-order-eu)
- [Partner EU cancellation API catalog](artifact/references/partner-eu-catalog.md)
- [API reference](artifact/references/api.md)
- [Temu access token guide](artifact/references/access-token.md)
- [Authorization flow](artifact/references/authorization-flow.md)
- [Temu Partner EU documentation](https://partner-eu.temu.com/documentation?menu_code=dbd3d395963a408984b8ae7dbc5f64f9)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, files]

**Output Format:** [Markdown guidance with shell commands and JSON request or response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full LinkFox and Temu responses under a local linkfox data directory and may print either full JSON or a summary depending on response size.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
