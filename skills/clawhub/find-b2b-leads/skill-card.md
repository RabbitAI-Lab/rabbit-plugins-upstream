## Description:

Find B2B leads by job title, company, and keyword, and return them as a structured list, powered by Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development teams use this skill to find people matching a role, company, and keyword profile, then use their profile details for outbound prospecting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lead search requires Cargo sign-in, sends search criteria for external processing, and uses credits.

Mitigation: Review the search criteria and sample results, and check the observed cost before approving a larger run.

Risk: A batch can apply credit costs across every record in its source list.

Mitigation: Start with a 10–20 record sample, report the hit rate and estimated full-run cost, and get approval before the larger run.

Risk: The skill's CLI install uses the latest package version, and the broader Cargo skill pack has not been reviewed as part of this release.

Mitigation: Prefer reviewed, fixed dependency versions and review the broader pack separately before adding it.

## Reference(s):

- [Cargo GTM skills project homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo prospecting recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/prospecting.md)

## Skill Output:

**Output Type(s):** [text, markdown]

**Output Format:** [Structured list or Markdown table of lead profiles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lead profiles include name, title, company, location, and LinkedIn URL; email addresses are not included. Results are returned in pages of 25.]

## Skill Version(s):

1.2.3 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
