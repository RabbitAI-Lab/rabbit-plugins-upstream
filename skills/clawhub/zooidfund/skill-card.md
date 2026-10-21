## Description:

Helps agents evaluate humanitarian campaigns on zooidfund and, with operator approval and a separate wallet skill, donate USDC on Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ales375](https://clawhub.ai/user/ales375)

### License/Terms of Use:

MIT-0

## Use Case:

Operators of OpenClaw or Hermes agents use this skill to browse humanitarian crowdfunding campaigns, assess unverified claims and available evidence, and plan or make authorized USDC donations on Base.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Campaign claims and uploaded evidence are unverified, so donations may support misleading campaigns.

Mitigation: Start with read-only review, assess claims and evidence critically, and require operator approval before donating.

Risk: USDC donations are irreversible, and scheduled actions can spend more than intended.

Mitigation: Use a dedicated low-balance wallet, require manual approval for registration and transfers, and set hard spending limits before scheduled use.

Risk: Agent identity, wallet transactions, and donation reasoning can become public; evidence may contain sensitive documents and incur per-request payments.

Mitigation: Review registration and terms with the operator, limit sensitive evidence access, and approve any paid requests explicitly.

Risk: An uncertain donation confirmation may leave a transfer sent but unrecorded.

Mitigation: Reconcile using the original transaction hash and campaign history; never resend USDC automatically.

## Reference(s):

- [Zooidfund Skill on ClawHub](https://clawhub.ai/ales375/skills/zooidfund)
- [Zooidfund](https://zooid.fund)
- [Zooidfund MCP endpoint](https://fcefnmdlggldmfusydix.supabase.co/functions/v1/mcp)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include campaign assessments, donation plans, and transaction status; a separate wallet skill sends funds.]

## Skill Version(s):

1.9.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
