## Description:

Reconcile vendor aliases into a canonical supplier name using registration data and suffix-aware matching.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations, procurement, and reconciliation teams use this skill to prepare reviewable supplier-name matching guidance for invoices, purchase requests, and vendor records that refer to the same supplier with different spellings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ambiguous supplier evidence could lead to an incorrect canonical supplier rule.

Mitigation: Review suggested canonicalization rules before applying them to business records, especially when identifiers conflict or evidence is ambiguous.

Risk: Name-only matching can be less reliable than stable registration or tax identifiers.

Mitigation: Compare registration or tax identifiers, country and registered address, and known aliases before relying on normalized supplier name text.

## Reference(s):

- [Supplier Name Resolution Guide on ClawHub](https://clawhub.ai/wxt-ai/skills/supplier-name-resolution-identifier)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [String]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns matching_guidance as a concise supplier canonicalization rule with the strongest evidence and review condition.]

## Skill Version(s):

1.0.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
