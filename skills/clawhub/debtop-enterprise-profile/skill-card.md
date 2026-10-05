## Description:

Builds an enterprise debt profile from public notices, summarizing disclosed amounts, related parties, timelines, guarantors, and collateral.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ninjaliang](https://clawhub.ai/user/ninjaliang)

### License/Terms of Use:

MIT-0

## Use Case:

Business analysts and other users can investigate a named company's disclosed debts, creditors, notice history, and security interests using linked public notices. The profile is not a credit report or a complete account of liabilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Guest access creates an identity and stores session data and a stable device identifier locally.

Mitigation: Prefer a platform-managed OAuth/MCP connector when available and restrict permissions on ~/.cache/debtop.

Risk: Queries contact an external service, and returned links carry client-source attribution.

Mitigation: Use only agent.debtop.com, do not provide an untrusted service endpoint, and review the client-source attribution.

Risk: Public notices can be incomplete or out of date, leading to misleading debt conclusions.

Mitigation: Cite notice links and query time, distinguish disclosed amounts from total liabilities, and verify the company identity before decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ninjaliang/skills/debtop-enterprise-profile)
- [Tools and fields](artifact/references/tools-and-fields.md)
- [Guest access](artifact/references/guest-access.md)
- [Errors and handling](artifact/references/errors.md)
- [Client source identifiers](artifact/references/client-source-ids.md)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown debt profile with tables and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes notice dates, disclosed amounts, related parties, and links to source notices; missing information is identified.]

## Skill Version(s):

1.0.5 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
