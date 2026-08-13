## Description:

Sorftime lets an agent query Sorftime through an OOMOL-connected account for Amazon product, keyword, category, review, sales, ranking, and credit research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and ecommerce operators use this skill to research Amazon products, keywords, categories, reviews, rankings, sales history, and Sorftime account usage from an agent environment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sorftime actions can consume paid requests or credits.

Mitigation: Review the selected action and its documented request cost before running high-volume or historical queries.

Risk: First-time setup may install the oo CLI, start OOMOL sign-in, or require connecting Sorftime credentials.

Mitigation: Run setup steps only after an auth or connection failure and confirm install or sign-in actions with the user.

Risk: Connector payloads may fail or query unintended data if built from stale assumptions.

Mitigation: Inspect the live action schema with `oo connector schema` before constructing each request payload.

## Reference(s):

- [Sorftime homepage](https://www.sorftime.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data payload and meta.executionId; many actions consume Sorftime requests or credits.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
