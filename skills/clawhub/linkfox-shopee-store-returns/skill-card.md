## Description:

Helps agents query and handle authorized Shopee store return and refund workflows through LinkFox scripts for the Shopee Open API Returns module.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, marketplace operators, and support agents use this skill to inspect Shopee return lists and details, handle seller return actions, manage disputes or offers, and upload or query return proof for authorized stores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a LinkFox API key and can access authorized Shopee store return data.

Mitigation: Install and run it only in environments where that API key and store data access are acceptable.

Risk: Write actions such as confirm, dispute, cancel_dispute, accept_offer, and proof uploads may change return or dispute state.

Mitigation: Require human confirmation with the exact shop and return_sn before running those actions.

Risk: Saved linkfox session files and payment QR files may contain sensitive store, payment, or account data.

Mitigation: Treat generated session files as sensitive and restrict where they are stored, shared, and retained.

Risk: Environment-variable URL overrides can redirect API traffic away from the normal LinkFox gateway.

Mitigation: Use URL overrides only in controlled development setups.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-returns)
- [Shopee Returns API documentation](https://open.shopee.com/documents/v2/v2.returns.get_return_list?module=102&type=1)
- [Returns module API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON API responses, and saved JSON data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large API responses are saved to a linkfox session data file and summarized on stdout unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
