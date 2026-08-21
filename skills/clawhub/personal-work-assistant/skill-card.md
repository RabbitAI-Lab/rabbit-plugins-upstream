## Description:

Personal Work Assistant aggregates Teambition tasks and DingTalk group, mention, all-hands, and direct-message activity into a concise daily action report with persistent task tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zpeng6834-arch](https://clawhub.ai/user/zpeng6834-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and workplace users use this skill to consolidate personal work tasks, DingTalk conversations, and Teambition assignments into a daily action-oriented morning report. It is intended for users who are authorized to process the connected workplace data sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill collects DingTalk group messages, direct messages, and Teambition task data that may include sensitive workplace information.

Mitigation: Install and run it only with explicit authorization for the configured conversations and projects, and restrict the monitored groups and direct-message collection to the minimum needed.

Risk: The skill can send collected workplace content to a hardcoded external AI service with bundled credentials.

Mitigation: Remove or rotate bundled credentials before use, configure an approved AI endpoint, and confirm organizational approval before sending message or task content outside the workspace.

Risk: The included setup can install a weekday cron job that repeatedly runs the assistant and pushes reports.

Mitigation: Review the scheduled job before enabling it, inspect it after setup, and remove or disable it when the assistant is no longer needed.

Risk: Configuration files may store user IDs, group IDs, profiles, and Teambition tokens in plaintext.

Mitigation: Move secrets to an approved secret store or environment-based configuration and avoid committing personalized config files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zpeng6834-arch/skills/personal-work-assistant)
- [Publisher Profile](https://clawhub.ai/user/zpeng6834-arch)

## Skill Output:

**Output Type(s):** [Markdown, Text, Shell commands, Configuration, Files]

**Output Format:** [Markdown daily report plus shell-based setup and YAML configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores task state in SQLite and can push the generated report to DingTalk.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
