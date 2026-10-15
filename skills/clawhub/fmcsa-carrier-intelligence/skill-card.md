## Description:

Helps vet US interstate motor carriers by USDOT or MC number using operating authority, insurance, safety history, and identity-linkage signals before tendering freight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kmcto](https://clawhub.ai/user/kmcto)

### License/Terms of Use:

MIT-0

## Use Case:

Freight brokers and carrier-vetting teams use this skill to review US motor carriers' operating authority, insurance filings, safety records, and identity signals before tendering freight. It offers free initial checks and optional paid lookups.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Carrier lookup queries are sent to a hosted service.

Mitigation: Confirm that sending USDOT or MC lookup queries to the service is acceptable before use.

Risk: Paid lookups can spend USDC through an x402 wallet.

Mitigation: Get user approval before the first paid call, check the quoted price, and track total spend.

Risk: Archived authority and insurance records may not reflect current status.

Mitigation: Report the record date and confirm current status with FMCSA or the insurer before relying on it.

## Reference(s):

- [FMCSA Carrier Intelligence homepage](https://kmcto.github.io/fmcsa-carrier-intelligence/)
- [FMCSA Carrier Intelligence agent reference](https://kmcto.github.io/fmcsa-carrier-intelligence/for-agents/)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown guidance with JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports record freshness and distinguishes identity signals from findings of fraud.]

## Skill Version(s):

1.2.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
