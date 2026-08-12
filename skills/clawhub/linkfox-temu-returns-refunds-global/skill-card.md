## Description:

Temu Global returns and refunds skill that helps agents call LinkFox gateway scripts for Partner Returns & Refunds and after-sales APIs, including after-sales order lookup, return logistics, return addresses, labels, signatures, and carrier queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Temu sellers, ecommerce operators, and developers use this skill to query and handle Global returns, refunds, and after-sales records through LinkFox gateway scripts. It supports operational review of return orders, refund summaries, labels, carriers, signatures, and saved JSON responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Temu API proxying can send arbitrary API types through the LinkFox gateway.

Mitigation: Use the generic proxy only for intended returns/refunds operations and review the requested type and params before execution.

Risk: Temu access tokens may be stored locally or printed in logs and transcripts.

Mitigation: Use saved tokens only on trusted machines, avoid plaintext token sharing, and rotate any token exposed in output or conversation history.

Risk: Saved response files can contain sensitive order, refund, address, or logistics data.

Mitigation: Protect the local linkfox data directory, avoid unnecessary --inline output, and remove saved response files when they are no longer needed.

Risk: Onboarding and billing flows may collect phone or OTP data and create payment orders.

Mitigation: Require explicit user confirmation before collecting phone or OTP data, saving credentials, or creating payment orders.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-returns-refunds-global)
- [API reference](references/api.md)
- [Temu access token authorization](references/access-token.md)
- [Authorization flow](references/authorization-flow.md)
- [Returns and Refunds API index](references/apis/README.md)
- [Partner Global catalog](references/partner-global-catalog.md)
- [Temu Partner Global documentation](https://partner-global.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python command examples and JSON responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are written under linkfox/<date>/<session>/data; large responses print summaries unless --inline is used.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
