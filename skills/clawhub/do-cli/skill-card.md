## Description:

Installs and guides use of the `do` CLI for capturing tasks, reviewing the day, updating tasks and habits, and reading life-tracking records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbeverhelst](https://clawhub.ai/user/robbeverhelst)

### License/Terms of Use:

MIT-0

## Use Case:

Personal AI agents use the CLI to manage a person's tasks, routines, habits, and selected life-tracking records. People can also use it directly to review and update that information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marked the skill suspicious because reported actions include personal-data writes and agent-thread posts; the scan was partial. Installation commands also run code fetched from the internet.

Mitigation: Review the security verdict and the commands needed for the task before installing. Use a scoped API key, and require user authorization before storing or changing personal information or posting to a thread. Install from a package or release source you trust.

## Reference(s):

- [Project documentation and source repository](https://github.com/robbeverhelst/do)
- [CLI releases](https://github.com/robbeverhelst/do/releases)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API responses]

**Output Format:** [Markdown instructions and shell examples; CLI results are JSON or human-readable text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the user's configured API key and its granted scopes.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
