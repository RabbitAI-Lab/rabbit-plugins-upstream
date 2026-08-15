## Description:

Turn a LinkedIn profile URL into a full person profile plus a verified work email in a single call, powered by Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external go-to-market teams, and agents use this skill when they already have LinkedIn profile URLs and need enriched person details plus verified work emails through Cargo and aiArk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkedIn profile URLs are sent to Cargo and aiArk for enrichment.

Mitigation: Confirm the user is comfortable with that data sharing before running enrichment.

Risk: Batch enrichment can consume Cargo credits at scale.

Mitigation: Sample 10-20 records first, report observed cost and hit rate, then get approval for the full batch size and estimated credits.

Risk: Running in the wrong Cargo account or workspace can expose data or charge the wrong workspace.

Mitigation: Confirm the active Cargo account and workspace before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/enrich-linkedin-profile)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo prospecting recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/prospecting.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown guidance with bash command blocks and CLI-returned enrichment results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a LinkedIn profile URL and an authenticated Cargo workspace; enrichment may consume Cargo credits.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
