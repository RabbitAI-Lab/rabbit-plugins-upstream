## Description:

Turn a LinkedIn profile URL into a full person profile plus a verified work email in a single call, powered by Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, sales operations teams, and go-to-market agents use this skill to enrich known LinkedIn profile URLs with profile details and a verified work email through Cargo and aiArk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkedIn profile URLs and enrichment results may contain personal data and are sent to Cargo and aiArk.

Mitigation: Use this workflow only with authorization and a lawful basis to process contact data.

Risk: The skill includes session-attribution behavior unrelated to the core enrichment task.

Mitigation: Review or remove the session-attribution command if additional telemetry or session stamping is not acceptable.

Risk: The skill may ask to star a GitHub repository using the user's GitHub account.

Mitigation: Ask once and act only after explicit user consent, or remove the repository-starring section.

Risk: Batch enrichment consumes Cargo credits and cost scales with record count.

Mitigation: Run a 10-20 record sample, report observed cost and hit rate, and get approval before a full batch.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/enrich-linkedin-profile)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo GTM prospecting recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/prospecting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands and CLI output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces enrichment guidance for LinkedIn URL inputs and instructs the agent to run Cargo CLI commands that may return profile data, company history, seniority, and verified email results.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
