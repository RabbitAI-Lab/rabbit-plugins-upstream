## Description:

Build a total addressable market list of companies filtered by industry, headcount, and geography, powered by Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations teams and sales leaders use this skill to size a target market and build company lists for an ideal customer profile. They filter companies by industry, headcount, and geography before deciding whether to enrich or pursue the list.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company searches incur credit charges that grow with the number of returned records.

Mitigation: Review the estimated full-run cost, start with a small sample, and get user approval before running the full list.

Risk: The bundled instructions install a CLI package, and the security verdict does not cover downloaded dependency code.

Mitigation: Review the exact package version and the broader skill pack before installing.

## Reference(s):

- [Cargo GTM Skills repository](https://github.com/getcargohq/gtm-skills)
- [Build TAM recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/build-tam.md)
- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/build-tam-list)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Company list, typically presented as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Company name, domain, headcount band, industry, and LinkedIn URL; results do not provide a total match count.]

## Skill Version(s):

1.2.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
