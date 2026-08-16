## Description:

Find every portfolio company of an investor or accelerator, then the people inside them, using Cargo and People Data Labs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, GTM, and research teams use this skill to list companies backed by a specific investor or accelerator and retrieve company domains or LinkedIn URLs for follow-on enrichment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using Cargo and People Data Labs through the Cargo CLI may involve external account login, possible stored credentials, workspace session attribution, and credit-consuming provider calls.

Mitigation: Confirm the user is comfortable with those services before install or login, check the account state with cargo-ai whoami, and make credit use visible before provider calls.

Risk: Broad provider runs can consume credits at scale.

Mitigation: Sample 10-20 records first, report observed cost and hit rate, then request approval with the record count and credit estimate before running the full batch.

## Reference(s):

- [Cargo GTM skills repository](https://github.com/getcargohq/gtm-skills)
- [Cargo portfolio prospecting recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/portfolio-prospecting.md)
- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/find-portfolio-companies)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, Configuration]

**Output Format:** [Markdown with Cargo CLI commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Cargo CLI, Cargo authentication, and People Data Labs provider access; includes sampling and approval guidance before broad credit-consuming runs.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
