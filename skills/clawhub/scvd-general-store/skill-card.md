## Description:

Guides agents through free x402 verification and commerce checks, payment troubleshooting, and user-authorized purchases at the SCVD General Store.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seancrecord](https://clawhub.ai/user/seancrecord)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to verify signed commerce artifacts, inspect endpoints, diagnose x402 payments, and test buyer or seller flows. With explicit user authorization, they can also make and recover real USDC purchases or use other store services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A live purchase may transfer real USDC, including when retrying a signed request.

Mitigation: Confirm the item, network and maximum spend with the user before signing; use an authorized wallet and never request wallet secrets.

Risk: A lost purchase response can lead to a duplicate payment if treated as a fresh checkout.

Mitigation: Recover using the original request and retry identity before authorizing any new payment.

Risk: Store posts, anchors, letters or optional telemetry may disclose private or identifying information.

Mitigation: Obtain the user's decision before posting or sending optional data, and omit sensitive content unless disclosure is intended.

## Reference(s):

- [SCVD General Store on ClawHub](https://clawhub.ai/seancrecord/skills/scvd-general-store)
- [SCVD Store](https://scvd.store)
- [Store catalogue and current terms](https://scvd.store/menu.json)
- [Verification guide](artifact/references/verification.md)
- [Purchases and recovery guide](artifact/references/purchases.md)
- [Buyer and seller testing guide](artifact/references/buyer-seller-testing.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code]

**Output Format:** [Markdown with links and request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should preserve the scope, exclusions, date and unobserved checks of any result.]

## Skill Version(s):

3.19.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
