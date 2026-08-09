## Description:

Temu Global order-management skill for querying and processing non-US/non-EU Temu orders through LinkFox-managed order APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to inspect Temu Global order lists, order details, shipping information, order amounts, combined shipment groups, customization details, and verification uploads through LinkFox gateway scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Temu order, shipping, and credential data.

Mitigation: Install only if you trust LinkFox with that data, run it in a controlled workspace, and treat saved response files as sensitive customer and order records.

Risk: The skill exposes broad proxy, onboarding/payment, token-printing, and persistent storage behavior beyond a tightly scoped Global order API.

Mitigation: Use only the specific order scripts needed for the task, and do not use generic proxy, token-printing, onboarding, or payment commands unless explicitly intended.

Risk: Gateway override environment variables can change where API traffic is sent.

Mitigation: Avoid setting gateway override environment variables except to known LinkFox endpoints.

Risk: Local token storage may persist Temu access tokens.

Mitigation: Protect or disable local token storage where possible and restrict access to the workspace and token store.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-order-global)
- [API reference](artifact/references/api.md)
- [Access token guide](artifact/references/access-token.md)
- [Order API index](artifact/references/apis/README.md)
- [Partner Global catalog](artifact/references/partner-global-catalog.md)
- [Onboarding and auth recovery](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with Python command examples and JSON API responses or saved response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full API responses under a linkfox session data directory and print either full JSON or a summary depending on response size.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
