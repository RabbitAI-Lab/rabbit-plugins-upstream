## Description:

Sorftime enables agents to run Amazon and Walmart keyword, product, category, sales, review, ranking, trend, and credit-usage research through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query Sorftime marketplace intelligence for Amazon and Walmart research, including keyword discovery, product details, sales history, rankings, reviews, category trends, and request or credit usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote pipe-to-shell installers that can execute changing code on the user's machine.

Mitigation: Review the oo CLI installer before running it, prefer an official pinned package or verified release where available, and only install after explicit user approval.

Risk: Sorftime requests route through OOMOL-connected credentials and can consume Sorftime request credits.

Mitigation: Connect Sorftime only when the user accepts that routing and credit usage; check usage or credit balance before costly research flows.

## Reference(s):

- [Sorftime homepage](https://www.sorftime.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Sorftime skill page](https://clawhub.ai/oomol/skills/oo-sorftime)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces oo CLI connector commands and summarizes JSON responses from Sorftime actions.]

## Skill Version(s):

1.0.1 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
