## Description:

Compares a sample of a ZoomInfo contact export with Cargo enrichment to measure verified coverage and credit costs before a renewal decision.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations and sales leaders use this skill to compare verified contact coverage from an existing ZoomInfo, Lusha, or Cognism export with Cargo results and estimate the cost of switching.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact records sent to Cargo and its waterfall providers may contain sensitive or restricted data.

Mitigation: Only use records you are authorized to send to those services.

Risk: A full-list enrichment can incur significant credit charges.

Mitigation: Start with 10–20 records, report the observed cost, and obtain approval before processing the full list.

Risk: The skill includes local session tracking and an optional GitHub repository star, which changes the user's public account state.

Mitigation: Review the tracking behavior and star only with the user's explicit consent.

Risk: The skill suggests installing a broader skill pack that has not been reviewed as part of this release.

Mitigation: Review the broader pack separately before installing it.

## Reference(s):

- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo waterfall provider playbook](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/provider-playbooks/waterfall.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands]

**Output Format:** [Markdown comparison with a table and optional CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports verified coverage on both sides and credits spent on the sample.]

## Skill Version(s):

1.0.1 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
