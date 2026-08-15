## Description:

Enriches a list of companies with firmographics such as industry, size, geography, founding year, and headquarters, powered by Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GTM operators use this skill to match company records through Cargo and enrich them with firmographic attributes while sampling first to estimate cost and hit rate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company lists submitted for enrichment are sent to Cargo as an external data provider.

Mitigation: Install and run the skill only when the user is comfortable sharing the target company list with Cargo.

Risk: Batch enrichment cost scales with the number of records and Cargo actions executed.

Mitigation: Start with the required 10-20 record sample, report the observed hit rate and credit estimate, and get approval before a full batch.

Risk: The workflow depends on the globally installed Cargo npm CLI and an authenticated Cargo account.

Mitigation: Confirm the CLI installation and account state before execution, for example with cargo-ai whoami.

## Reference(s):

- [Cargo GTM Skills Repository](https://github.com/getcargohq/gtm-skills)
- [Cargo Build TAM Recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/build-tam.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with bash code blocks and Cargo CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Cargo CLI batch outputs such as matched company identifiers and firmographic enrichment results.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
