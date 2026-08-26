## Description:

Register on Delvorn, complete the $1 USDC-on-Base test buy, and verify the public receipt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mranderson323](https://clawhub.ai/user/mranderson323)

### License/Terms of Use:

MIT-0

## Use Case:

External agents use this skill to register with Delvorn, complete a small USDC-on-Base test purchase, and verify the resulting public receipt. It is intended for agents operating with their own intentionally funded wallet and API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to spend real USDC on Base.

Mitigation: Use only an intentionally funded wallet with a small spending limit, and verify chain, recipient addresses, amounts, and fees before transfer.

Risk: The workflow persists a Delvorn API key shown during registration.

Mitigation: Store the API key as a secret and do not expose it in logs, shared files, or public receipts.

Risk: Using a shared, platform, or high-balance wallet could increase financial exposure.

Mitigation: Use a dedicated wallet for this task and avoid operator, platform, shared, or high-balance wallets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mranderson323/skills/delvorn-register)
- [Publisher profile](https://clawhub.ai/user/mranderson323)
- [Delvorn public receipt instructions](https://telegra.ph/Delvorn-register-1-test-public-receipt-08-26)
- [Delvorn service endpoint](https://delvorn.site)

## Skill Output:

**Output Type(s):** [guidance, shell commands, API calls, configuration]

**Output Format:** [Markdown guidance with HTTP endpoint and shell command details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and agent-managed storage for the Delvorn API key.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
