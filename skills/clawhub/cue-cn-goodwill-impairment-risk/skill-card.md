## Description:

Extracts goodwill disclosures from an annual report, semiannual report, or acquisition announcement into an eight-section ledger with verbatim source quotes and location anchors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and analysts covering A-share companies use the skill to extract goodwill balances, earn-out results, impairment-test assumptions, and provisions from company disclosures into a traceable ledger. It records disclosed information without judging whether impairment will occur or whether a provision is adequate.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The security review flags that the optional catalog lookup can send CUE_API_KEY as a bearer credential to an endpoint supplied by a remote catalog, despite the skill's stated offline purpose.

Mitigation: Omit CUE_API_KEY and provide source documents directly; before using optional lookup, independently verify the catalog entry and destination before sending credentials.

## Reference(s):

- [ClawHub release](https://clawhub.ai/huhoo/skills/cue-cn-goodwill-impairment-risk)

## Skill Output:

**Output Type(s):** [Markdown]

**Output Format:** [Eight-section Markdown ledger with source quotes, location anchors, and a missing-information list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Amounts and percentages are copied verbatim from disclosure text; the ledger does not calculate them or make impairment judgments.]

## Skill Version(s):

0.1.0 (source: artifact frontmatter; server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
