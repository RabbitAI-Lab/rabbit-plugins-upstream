## Description:

Provides agent guidance and Python helpers for Temu US buyer and seller order-cancellation workflows through the LinkFox gateway, including after-sales cancel list and agree actions, seller appeals, and out-of-stock cancellation APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Temu sellers, operators, and developers use this skill to prepare and run US cancellation API calls for buyer after-sales cancellation approval and seller appeal or out-of-stock cancellation workflows through LinkFox.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The skill requires Temu and LinkFox account access and can perform mutating order-cancellation actions.

Mitigation: Use it only in a trusted environment with authorized accounts, and confirm order identifiers and intended cancellation actions before running apply or agree scripts.

Risk: Local token storage and full response logging can expose account tokens, order data, or customer-related operational data.

Mitigation: Do not commit LinkFox output directories or Temu token files, and restrict filesystem access to users who are allowed to view the associated account data.

Risk: Endpoint override variables and generic proxy or download helpers can send requests or signed URLs outside the normal workflow.

Mitigation: Use default endpoints unless you control the destination, and review proxy and file-download parameters before execution.

Risk: The security scan summary notes broader account, payment/onboarding, download, and generic proxy capabilities beyond a narrow cancel-order workflow.

Mitigation: Review onboarding and billing-related prompts before use, and grant this skill only where those broader capabilities are acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-cancel-order-us)
- [Temu US Cancel Order API Reference](references/api.md)
- [Partner US Cancel Order Catalog](references/partner-us-catalog.md)
- [Temu Access Token Guide](references/access-token.md)
- [Temu Authorization Flow](references/authorization-flow.md)
- [Temu Partner US Documentation](https://partner-us.temu.com/documentation)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, JSON files]

**Output Format:** [Markdown guidance, Python command examples, stdout JSON or summaries, and full JSON responses saved to local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Small responses print inline; larger responses print summaries unless inline output is requested, while complete responses are written under a LinkFox session data directory.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
