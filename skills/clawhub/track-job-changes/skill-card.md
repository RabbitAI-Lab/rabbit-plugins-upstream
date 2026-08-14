## Description:

Detects which existing contacts have changed jobs and where they moved, using Cargo's waterfall provider.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

GTM, sales, and RevOps teams use this skill to check existing contacts for job changes, identify moved champions, and decide whether to run larger monitored batches after sampling cost and hit rate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected contact emails and company domains to Cargo and its waterfall provider for enrichment.

Mitigation: Install and run it only when that data sharing is acceptable for the selected contacts.

Risk: Large, repeated, or scheduled runs can consume Cargo credits.

Mitigation: Start with the documented small sample, confirm observed cost and hit rate, and require explicit approval before larger batches.

Risk: The workflow depends on installing and authenticating Cargo's external CLI.

Mitigation: Confirm comfort with the Cargo CLI and authentication requirements before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cargo-ai/skills/track-job-changes)
- [Cargo GTM Skills Homepage](https://github.com/getcargohq/gtm-skills)
- [Job Change Monitoring Recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/job-change-monitoring.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured job-change statuses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces MOVED, LEFT, NO_CHANGE, or UNKNOWN status guidance per contact, with cost and approval guidance for batches.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
