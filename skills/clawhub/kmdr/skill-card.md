## Description:

Kmoe Manga Downloader helps agents search Kmoe manga, estimate and start downloads, track background progress, and manage credentials and download configuration through the kmdr CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrisis58](https://clawhub.ai/user/chrisis58)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate the kmdr command-line downloader for Kmoe manga search, quota-aware download planning, background download monitoring, and credential pool configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account passwords may be exposed if users paste credentials into the agent conversation.

Mitigation: Prefer terminal-based login outside chat, and avoid sharing passwords with the agent.

Risk: Background downloads can consume account quota or write to an unexpected destination.

Mitigation: Confirm the configured destination and available quota before starting background downloads.

Risk: The skill depends on the external kmoe-manga-downloader package.

Mitigation: Review the external package before installation and keep the installed version within the documented supported range.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrisis58/skills/kmdr)
- [Kmoe website](https://kxx.moe/)
- [JSON output format](references/output-format.md)
- [Error status codes](references/error-codes.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured JSON or NDJSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses kmdr toolcall-mode result and progress records; background downloads return task IDs for later status checks.]

## Skill Version(s):

1.0.0-a4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
