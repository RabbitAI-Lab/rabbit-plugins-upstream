## Description:

Helps vet US interstate motor carriers by USDOT number using authority, insurance, safety, and identity-linkage signals before freight is tendered.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kmcto](https://clawhub.ai/user/kmcto)

### License/Terms of Use:

MIT-0

## Use Case:

Freight brokers, shippers, and their agents use the skill to screen US motor carriers, investigate identity links, and review authority, insurance, and safety history before tendering freight. It supports vetting, not a final finding of fraud or legal compliance.

### Deployment Geography for Use:

United States (US interstate motor-carrier data)

## Known Risks and Mitigations:

Risk: Paid lookups may spend USDC or use evaluation credit without intended authorization.

Mitigation: Try free tools first; obtain user approval before a paid lookup, verify the quoted amount, and track spending.

Risk: Snapshot or legacy-sourced authority and insurance records may be stale.

Mitigation: Report the record date and verify time-sensitive status directly with FMCSA or the insurer.

Risk: Identity-linkage flags may be mistaken for proof of fraud.

Mitigation: Treat flags as leads for further review and communicate their stated confidence caveats.

## Reference(s):

- [FMCSA Carrier Intelligence homepage](https://kmcto.github.io/fmcsa-carrier-intelligence/)
- [FMCSA Carrier Intelligence agent reference](https://kmcto.github.io/fmcsa-carrier-intelligence/for-agents/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with optional API request examples and carrier-vetting summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports record freshness and distinguishes identity signals from findings of fraud.]

## Skill Version(s):

1.3.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
