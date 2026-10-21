## Description:

Turn a LinkedIn profile URL into a full person profile plus a verified work email in a single call, powered by Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development and account teams use LinkedIn profile URLs to obtain person and company details alongside verified work emails for prospecting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkedIn profile data is sent to an external enrichment service using Cargo CLI authentication.

Mitigation: Confirm authorization to share the profiles and review the service and authentication requirements before use.

Risk: The skill sends session attribution to Cargo and offers a post-task GitHub star action.

Mitigation: Review the attribution step before running it; never star a repository without the user's explicit consent.

Risk: The optional broader skill-pack installation uses an unpinned npx command.

Mitigation: Avoid that optional installation unless the package and broader skill pack have been separately reviewed and trusted.

Risk: Enrichment batches can incur credits proportional to the number of successful records.

Mitigation: Test a small sample, report the hit rate and estimated credits, and get approval before a full batch.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/enrich-linkedin-profile)
- [Project homepage (listed in skill metadata)](https://github.com/getcargohq/gtm-skills)
- [Cargo prospecting recipe (linked by skill)](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/prospecting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Profile and email results as structured records or a Markdown table, with CLI commands for enrichment]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A record may be empty when no verified email is found.]

## Skill Version(s):

1.1.3 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
