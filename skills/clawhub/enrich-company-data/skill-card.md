## Description:

Enrich a list of companies with firmographics — industry, size, geography, founding year, and headquarters, powered by Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations and sales development teams can enrich authorized company domains with firmographics, including industry, headcount, geography, founding year, and headquarters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitting company domains may disclose information to Cargo and aiArk.

Mitigation: Submit only domains you are authorized to share with both providers.

Risk: A batch fans out across every supplied record, so a full run can incur cost proportional to the list size.

Mitigation: Test 10–20 records first, report the observed cost and hit rate, and obtain approval for the full run using its record count and credit estimate.

Risk: The CLI dependency is unpinned and its implementation was not audited in this assessment.

Mitigation: Review the broader skill pack and dependency before installing or running the CLI.

## Reference(s):

- [Cargo GTM skills repository](https://github.com/getcargohq/gtm-skills)
- [Build TAM recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/build-tam.md)
- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/enrich-company-data)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown guidance, shell commands, and tabular company firmographic data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Company fields may remain empty when no match is found.]

## Skill Version(s):

1.1.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
