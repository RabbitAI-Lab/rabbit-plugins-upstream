## Description:

Enriches company domains with industry, headcount, geography, founding year, and headquarters using Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development and revenue operations teams use this skill to enrich lists of company domains with firmographic data for prospecting and account analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the Cargo CLI globally and sending company domains to Cargo may conflict with local software or data-sharing policies.

Mitigation: Review installation commands and approve the service and data transfer before use.

Risk: Batch enrichment consumes credits across every submitted record.

Mitigation: Test 10–20 domains, report hit rate and estimated credits, and obtain approval before a full batch.

Risk: The workflow inspects local agent configuration and creates Cargo workspace attribution and persistent star-prompt tracking unrelated to enrichment.

Mitigation: Review these optional side effects and omit them if they are not needed or authorized.

Risk: The optional GitHub star action uses the user's account for publisher promotion.

Mitigation: Omit the star step unless the user explicitly agrees after the work is complete.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/enrich-company-data)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo enrichment recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/build-tam.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown table of enriched company records with supporting shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Unmatched companies may have blank fields; enrichment consumes credits per record.]

## Skill Version(s):

1.1.2 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
