## Description:

Helps agents manage Shopee shop vouchers through LinkFox's Shopee developer proxy, covering creation, listing, detail lookup, updates, early ending, and deletion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and marketplace operators use this skill to manage authorized Shopee store voucher campaigns from an agent workflow, including creating, reviewing, updating, ending, and deleting vouchers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can manage live Shopee voucher state, including add, update, end, and delete actions.

Mitigation: Manually confirm intended shop, voucher, and operation details before executing any state-changing action.

Risk: The skill uses a LinkFox API key and may guide SMS login, API-key generation, and payment-order creation.

Mitigation: Use only trusted account credentials, avoid sharing verification codes unless account onboarding is intended, and confirm billing actions before placing orders.

Risk: The skill saves full API responses locally, which may include operational shop or voucher data.

Mitigation: Run it in an appropriate workspace and review saved response files before sharing or committing generated output.

## Reference(s):

- [Shopee voucher API reference](references/api.md)
- [Voucher onboarding and billing guidance](references/onboarding.md)
- [Shopee Open Platform add_voucher documentation](https://open.shopee.com/documents/v2/v2.voucher.add_voucher?module=112&type=1)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-voucher)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance, JSON files]

**Output Format:** [Markdown guidance with inline shell commands and saved JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under ./linkfox/<date>/<session>/data; large responses print summaries unless inline output is requested.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
