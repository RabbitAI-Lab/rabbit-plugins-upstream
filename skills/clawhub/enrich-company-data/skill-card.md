## Description:

Enriches company domains with industry, headcount, geography, founding year, and headquarters information using Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and revenue operations teams enrich company-domain lists with firmographics for account research and planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company domains are sent to Cargo, and batch enrichment can consume credits.

Mitigation: Confirm data-sharing approval; test 10–20 records, report coverage and estimated credits, and obtain approval before a full batch.

Risk: The skill includes attribution that inspects local agent configuration and a separate GitHub star request.

Mitigation: Review or remove these optional steps if only enrichment is needed; never star without explicit user consent.

Risk: Installing the latest CLI version without a pin can change behavior between deployments.

Mitigation: Pin and review the CLI version before installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/enrich-company-data)
- [Cargo skill homepage (publisher-provided; import provenance unavailable)](https://github.com/getcargohq/gtm-skills)
- [Cargo company-data workflow reference](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/build-tam.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with a company firmographics table and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Unmatched companies may have empty fields; report observed coverage and credit usage.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
