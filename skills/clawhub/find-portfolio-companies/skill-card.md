## Description:

Find an investor's or accelerator's portfolio companies and prepare the list for people research using Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Account executives and sales development teams use this skill to find companies backed by a named investor or accelerator and prepare the company list for people research and outreach planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broad search can consume credits for every returned company.

Mitigation: Start with a 10–20 company sample, report the estimated cost, and expand only after the user approves the full search.

Risk: The workflow relies on an external CLI and related skill pack whose downloaded code is outside this artifact review.

Mitigation: Review and pin the external CLI and any broader skill pack before use.

## Reference(s):

- [Cargo GTM skills repository](https://github.com/getcargohq/gtm-skills)
- [Portfolio prospecting recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/portfolio-prospecting.md)

## Skill Output:

**Output Type(s):** [Company data, Shell commands]

**Output Format:** [Structured portfolio company records with domains, LinkedIn URLs, and investor details, plus inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Searches are capped by a result limit and cost 0.5 credits per returned company.]

## Skill Version(s):

1.0.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
