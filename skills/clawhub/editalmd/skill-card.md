## Description:

Helps agents research Brazilian public tenders, compare winning prices, read procurement documents, and track new opportunities through EditalMD.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wrpbr](https://clawhub.ai/user/wrpbr)

### License/Terms of Use:

MIT-0

## Use Case:

Suppliers and procurement researchers use this skill to find Brazilian public tenders, review deadlines, prices and qualification requirements, and monitor opportunities. Some document access uses prepaid credits with the user's approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid document access can consume prepaid credits.

Mitigation: Show the document quote and obtain user approval before requesting paid access; let the user purchase credits on the site.

Risk: Access codes and alert or payment tokens could expose private access if shared.

Mitigation: Treat access codes and cred_, edm_ and whsec_ tokens as secrets; do not include them in files, logs or responses.

Risk: Estimated deadlines or automatically processed documents may be incomplete or inaccurate.

Mitigation: Confirm deadlines and requirements against the original tender document and check dossier coverage before relying on it.

## Reference(s):

- [EditalMD ClawHub release](https://clawhub.ai/wrpbr/skills/editalmd)
- [EditalMD API documentation](https://editalmd.com/llms-full.txt)
- [EditalMD API discovery](https://editalmd.com/api/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown with tender details, document excerpts and page references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include estimated challenge deadlines and links to purchase records.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
