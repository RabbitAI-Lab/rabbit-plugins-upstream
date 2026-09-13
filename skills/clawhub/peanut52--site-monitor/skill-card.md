## Description:

Monitor websites for uptime and content changes. Use when checking if a URL is online, detecting page modifications, or tracking HTTP status codes over time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[peanut52](https://clawhub.ai/user/peanut52)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site operators use this skill to check whether a URL is online, detect page content changes, and track HTTP status codes over time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make HTTP requests from the user's machine to user-provided URLs.

Mitigation: Run it in a restricted environment and avoid internal or metadata-service URLs.

Risk: The skill writes a local state file and allows the state-file path to be supplied.

Mitigation: Use a dedicated private state directory and do not pass sensitive paths to --state-file.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/peanut52/skills/site-monitor)
- [Publisher profile](https://clawhub.ai/user/peanut52)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration]

**Output Format:** [Plain text status messages and command-line usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write a local JSON state file to compare content hashes across checks.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
