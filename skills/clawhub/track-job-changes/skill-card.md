## Description:

Detects whether existing contacts have changed jobs and where they moved using Cargo's Waterfall provider.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and account teams check existing contacts for job changes and identify their new companies and roles. Start with a small segment before approving a larger credit-consuming batch.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact emails and company domains are sent to Cargo/Waterfall for job-change lookups.

Mitigation: Use only contacts approved for third-party processing and limit the records sent.

Risk: The installation instruction uses the mutable latest release of the Cargo CLI.

Mitigation: Review and pin a trusted CLI version before installation.

Risk: The skill creates a Cargo session attribution record and checks local agent configuration.

Mitigation: Review or omit the attribution and local-configuration steps if they are unnecessary.

Risk: The skill suggests an unrelated GitHub starring action using the user's account.

Mitigation: Skip the starring step unless the user explicitly requests it.

Risk: Large or scheduled batches consume credits per contact and per run.

Mitigation: Sample 10–20 contacts, report observed cost, and obtain approval before running the full batch.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/track-job-changes)
- [Homepage listed in skill metadata](https://github.com/getcargohq/gtm-skills)
- [Job-change monitoring recipe linked by the skill](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/job-change-monitoring.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with CLI commands and a per-contact results table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes MOVED, LEFT, NO_CHANGE, and UNKNOWN results and estimates credits before a full batch.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
