## Description:

Temu 美国站-订单 helps agents call LinkFox gateway scripts for Temu Partner US order list, order detail, shipping address, amount, combined-shipment, customization, and SN/IMEI verification upload workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to retrieve and manage Temu US order and shipping data through LinkFox-mediated Partner US API calls. It supports order lookup, address retrieval or decryption, reconciliation amounts, combined shipment groups, customization data, and verification uploads.

### Deployment Geography for Use:

United States (Temu Partner US workflows)

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys and Temu access tokens.

Mitigation: Install only when LinkFox is trusted, keep credentials out of shared transcripts and logs, rotate exposed tokens, and restrict access to environment variables and ~/.linkfox token files.

Risk: Order workflows can expose customer PII including decrypted addresses, phone numbers, SN/IMEI values, and saved response files.

Mitigation: Run only for authorized business purposes, request the minimum data needed, avoid pasting sensitive output into unrelated contexts, and delete local response files when no longer required.

Risk: Generic proxy, payment, and onboarding commands may perform broader account or billing actions than a narrow order lookup.

Mitigation: Use the generic proxy and payment/onboarding commands only when explicitly needed, review parameters before execution, and confirm any action that can affect account balance or billing.

Risk: The security verdict is suspicious due to sensitive-data handling, broad gateway forwarding, and persistent local storage.

Mitigation: Review the skill and its arguments before deployment, scan updates before installing, and regularly inspect or remove local linkfox output folders and token stores.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-order-us)
- [API reference](references/api.md)
- [Access token guidance](references/access-token.md)
- [Partner US order catalog](references/partner-us-catalog.md)
- [Order API index](references/apis/README.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [Temu Partner US documentation](https://partner-us.temu.com/documentation)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands and JSON request or response data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full JSON responses to local linkfox output folders and may print JSON or summaries to stdout; --inline can force full stdout output.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
