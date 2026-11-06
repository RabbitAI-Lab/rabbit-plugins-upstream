## Description:

Creates videos, images, voiceovers, music, narrated shorts, and captioned clips through Treza's paid media services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[treza-labs](https://clawhub.ai/user/treza-labs)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents can create or edit media for social posts, presentations, and other projects, including turning long videos into short captioned clips. The workflow guides users through reviewing content and price before a paid request.

### Deployment Geography for Use:

Global, excluding sanctioned or unsupported regions.

## Known Risks and Mitigations:

Risk: Paid media requests spend USDC, and the submitted prompt, text, topic, or source link is sent to Treza and its rendering provider.

Mitigation: Review the request and current quoted price with the user before sending it; cap payment at the approved amount and fund the wallet only for intended spending.

Risk: Wallet sign-in sends the user's email and one-time code to Coinbase; Treza may retain wallet-linked purchase records and content, and media links may be accessible to anyone who holds them.

Mitigation: Explain the Coinbase sign-in disclosure and obtain the user's agreement before login. Avoid sending sensitive content, and review Treza's Privacy Policy before use.

Risk: The external wallet software and remote rendering services have not been audited.

Mitigation: Use only the pinned wallet CLI version documented by the skill, check the request and price before payment, and limit wallet funds to intended spending.

## Reference(s):

- [Treza x402 media service](https://www.trezalabs.com/x402)
- [Treza media skill release](https://clawhub.ai/treza-labs/skills/treza)

## Skill Output:

**Output Type(s):** [Media files, Text, JSON]

**Output Format:** [Video, image, or audio file URLs with JSON result/status data and optional titles, descriptions, or captions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media is rendered remotely; paid calls use USDC.]

## Skill Version(s):

1.0.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
