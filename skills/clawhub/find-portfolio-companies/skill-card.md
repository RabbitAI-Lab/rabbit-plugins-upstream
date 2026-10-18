## Description:

Finds an investor's or accelerator's portfolio companies and identifies people at those companies using Cargo and TheirStack.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and business-development teams use this skill to find companies backed by a target investor or accelerator and identify prospects for warm introductions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill records Cargo session attribution and checks local agent configuration.

Mitigation: Review these steps before installing or running the skill if local configuration checks or vendor attribution are unwanted.

Risk: Cargo login persists locally, and the skill can prompt for a public GitHub star.

Mitigation: Use a suitable account, and approve a GitHub star only if you explicitly want that account change.

Risk: Installing the latest CLI release can change the code executed; larger searches consume more credits.

Mitigation: Pin the CLI version when stricter supply-chain control is needed, and approve a small sample and its estimated cost before expanding the search.

## Reference(s):

- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Portfolio prospecting recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/portfolio-prospecting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown portfolio-company list or table with prospecting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Company records may include domains, industries, employee counts, LinkedIn URLs, and investor names; searches consume credits per returned company.]

## Skill Version(s):

1.0.2 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
