## Description:

Helps agents query and manage Shopee store return and refund workflows through LinkFox's Shopee Returns API scripts, including return lists, details, confirmations, disputes, offers, proof uploads, and reverse tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and support agents use this skill to inspect and act on Shopee store return and refund cases after the store authorization dependency is available. It is suited for workflows that require return detail lookup, seller decisions, dispute handling, proof upload, or reverse-logistics tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a LinkFox API key and can call live Shopee return and refund APIs through LinkFox.

Mitigation: Install only after reviewing the skill, store API keys in the documented environment variables, and require explicit user confirmation before live return, refund, dispute, offer, or proof-upload actions.

Risk: The bundled onboarding flow can perform phone/SMS login, API-key generation, and payment-order steps.

Mitigation: Use onboarding only when account setup or billing is intentionally part of the task, and ask the user before sending codes, logging in, generating keys, creating orders, or presenting payment options.

Risk: Full API responses are written to local session files and may contain sensitive store, return, buyer, logistics, or dispute data.

Mitigation: Keep generated response files in an appropriate workspace, limit sharing of saved JSON outputs, and remove files that are no longer needed under the user's data-retention policy.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-returns)
- [Shopee Returns API reference](https://open.shopee.com/documents/v2/v2.returns.get_return_list?module=102&type=1)
- [LinkFox returns API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON files]

**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are persisted under a linkfox session data directory; small responses may also be printed inline, while larger responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
