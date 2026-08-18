## Description:

Detect which of your contacts have changed jobs, and where they went, powered by Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, customer success, and go-to-market teams use this skill to check existing contacts for job-change signals and identify where movers went. It is intended for targeted CRM or contact-list checks rather than broad lead sourcing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends contact data to Cargo during the job-change lookup workflow.

Mitigation: Review data-sharing expectations and confirm the contact sample or segment before running Cargo CLI commands.

Risk: The workflow writes a Cargo session attribution record.

Mitigation: Inform users that Cargo may receive session attribution metadata before running the attribution command.

Risk: The skill includes a post-task prompt that may use the user's GitHub account to star the publisher repository.

Mitigation: Only perform the GitHub star action after the user gives explicit consent, and skip it when GitHub CLI is unavailable or unauthenticated.

Risk: Running the lookup across large contact lists can consume credits quickly.

Mitigation: Start with a 10-20 record sample, report observed cost and hit rate, then ask for approval before scaling to the full list.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/track-job-changes)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo job-change monitoring recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/job-change-monitoring.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline bash code blocks and plain-text result interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Cargo CLI commands, cost guidance, and job-change status interpretation for contact records.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
