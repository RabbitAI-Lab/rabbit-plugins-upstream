## Description:

Guides agents through discovering and paying for individual x402 or MPP service calls with the Nevermined Router, within a delegated spending budget.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find compatible services, quote and purchase individual calls through Nevermined, and review spending against a capped delegation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-initiated payments can spend real funds.

Mitigation: Start in the sandbox, use short-lived delegations with small spending caps, and quote the full price before paying.

Risk: A leaked Nevermined API key can expose account access.

Mitigation: Keep NVM_API_KEY private and never forward it to a merchant.

Risk: Raw URLs and forwarded merchant headers can disclose request data to third-party services.

Mitigation: Review target URLs, request bodies, and merchant-auth headers before sending a paid request.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/nevermined-io/skills/nevermined-router)
- [Nevermined Router documentation](https://nevermined.ai/docs/products/catalog/router/overview)
- [Nevermined API key portal](https://nevermined.app)
- [Bootstrap and delegation](references/bootstrap.md)
- [Paying and quoting](references/paying.md)
- [Errors and guardrails](references/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with HTTP and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructional content; executing paid requests requires a Nevermined API key and a funded, capped delegation.]

## Skill Version(s):

0.1.37 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
