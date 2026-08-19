## Description:

Builds a total addressable market list of companies filtered by industry, headcount, and geography using Cargo's Sales Navigator integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and go-to-market teams use this skill to size and build target-account company lists by industry, headcount, and geography before downstream enrichment or outreach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cargo session attribution may send session-source metadata to Cargo.

Mitigation: Review or skip the attribution session upsert before running the workflow if you do not want Cargo to receive that metadata.

Risk: The skill includes a GitHub starring flow that can act through the user's GitHub account.

Mitigation: Only perform the star action after explicit user consent, and skip it entirely if the user does not want to endorse the repository.

Risk: Cargo CLI actions can consume credits, and large batches can scale cost quickly.

Mitigation: Run a small sample first, report observed cost and hit rate, and request approval with a credit estimate before expanding the run.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cargo-ai/skills/build-tam-list)
- [Cargo GTM Skills Homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo Build TAM Recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/build-tam.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Guidance, Text]

**Output Format:** [Markdown with inline bash code blocks and CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return company account records such as name, domain, headcount band, industry, and LinkedIn URL through Cargo CLI execution.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
