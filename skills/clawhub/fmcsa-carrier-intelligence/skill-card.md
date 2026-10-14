## Description:

Helps vet US interstate motor carriers by USDOT number using authority, insurance, safety, and identity signals, with free previews and optional paid queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kmcto](https://clawhub.ai/user/kmcto)

### License/Terms of Use:

MIT-0

## Use Case:

Freight brokers and carrier-vetting teams use this skill to review a US motor carrier's operating authority, insurance, safety history, and identity signals before tendering freight. It supports follow-up investigation rather than treating identity flags as proof of fraud.

### Deployment Geography for Use:

Global (US interstate motor carrier records)

## Known Risks and Mitigations:

Risk: Queries send carrier information to the publisher's hosted service.

Mitigation: Review the data being sent and use free previews before choosing paid calls.

Risk: Paid queries transfer USDC on Solana through x402.

Mitigation: Require explicit approval before the first paid call, confirm the quoted amount, and track total spending.

Risk: Monthly snapshots and identity flags can be stale or falsely suggest fraud.

Mitigation: Report the record date and corroborate flags independently before making decisions.

## Reference(s):

- [FMCSA Carrier Intelligence documentation](https://kmcto.github.io/fmcsa-carrier-intelligence/)
- [Agent reference](https://kmcto.github.io/fmcsa-carrier-intelligence/for-agents/)
- [ClawHub skill release](https://clawhub.ai/kmcto/skills/fmcsa-carrier-intelligence)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes record freshness and caveats for identity signals when available.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
