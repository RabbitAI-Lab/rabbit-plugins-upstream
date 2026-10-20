## Description:

Helps agents search Brazilian public tenders, review procurement records and documents, and monitor opportunities through EditalMD.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wrpbr](https://clawhub.ai/user/wrpbr)

### License/Terms of Use:

MIT-0

## Use Case:

Suppliers, procurement teams, and their agents use this skill to find Brazilian public tenders, check deadlines and winning prices, review tender requirements, and track new opportunities.

### Deployment Geography for Use:

Brazil

## Known Risks and Mitigations:

Risk: Procurement queries and document identifiers are sent to editalmd.com.

Mitigation: Confirm the user is comfortable sharing those queries and identifiers with EditalMD before use.

Risk: Access codes and credit or owner tokens can expose paid features or private account access.

Mitigation: Keep access codes and cred_, edm_, and whsec_ tokens private; use paid features only with user-provided authorization.

Risk: Estimated challenge deadlines or incomplete document analysis may be inaccurate.

Mitigation: Confirm deadlines and qualification requirements against the original tender documents before acting.

## Reference(s):

- [EditalMD skill on ClawHub](https://clawhub.ai/wrpbr/skills/editalmd)
- [EditalMD API reference](https://editalmd.com/llms-full.txt)
- [EditalMD free evaluation guide](https://editalmd.com/avaliacao.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown summaries with document excerpts and source references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tender dates, price summaries, qualification requirements, and page evidence.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
