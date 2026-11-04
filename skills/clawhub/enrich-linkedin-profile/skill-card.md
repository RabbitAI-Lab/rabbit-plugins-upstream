## Description:

Enriches a LinkedIn profile URL into a person profile and verified work email through Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development and account teams use it to enrich LinkedIn URLs they are authorized to share with Cargo and aiArk, retrieving profile details and a verified work email for outreach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact profiles and work emails contain personal data that is sent to an enrichment provider.

Mitigation: Submit only contacts authorized for sharing with Cargo and aiArk.

Risk: A full batch can create costs across every submitted record.

Mitigation: Sample 10–20 records, review the observed cost and hit rate, and get approval before running the full batch.

Risk: Installing the CLI or optional skills pack introduces external packages and code.

Mitigation: Review external packages and the optional skills pack before installing them.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/cargo-ai/skills/enrich-linkedin-profile)
- [Cargo project homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo prospecting recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/prospecting.md)

## Skill Output:

**Output Type(s):** [Structured data, Text]

**Output Format:** [Person profile fields and a verified work email returned by the Cargo CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A miss may return an empty result with no profile when no email is found.]

## Skill Version(s):

1.1.4 (source: SKILL.md frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
