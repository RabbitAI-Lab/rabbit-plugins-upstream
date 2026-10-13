## Description:

Automates meeting preparation and daily development summaries by checking Google Calendar for upcoming meetings, generating standup updates from GitHub commits, and formatting developer-friendly summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hougangdev](https://clawhub.ai/user/hougangdev)

### License/Terms of Use:


## Use Case:

Developers and engineering teams use this skill to prepare for upcoming meetings with commit-based updates and to produce end-of-day summaries across configured repositories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests calendar and GitHub credentials that may expose sensitive meeting or repository data if over-scoped.

Mitigation: Use read-only Calendar access, a fine-grained GitHub token or GitHub App limited to the exact repositories needed, and secure secret storage instead of project-local plaintext files.

Risk: Scheduled summaries can distribute team-wide commit or meeting context without clear audience and scope controls.

Mitigation: Define explicit allowlists for calendars, repositories, developers, recipients, and schedules before enabling automated notifications or summaries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hougangdev/skills/meeting-prep)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Plain text summaries with shell command examples and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Meeting updates and daily summaries group commit information by repository, subdirectory, and author.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
