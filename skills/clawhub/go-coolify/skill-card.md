## Description:

Guides Go developers in using the unofficial go-coolify client to work with Coolify API resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write and check Go integrations that inspect or, when requested, change resources on their Coolify instance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An API token could be exposed or sent to the wrong Coolify instance.

Mitigation: Keep the token out of code and logs, and confirm the HTTPS instance URL before sending credentials.

Risk: Create, update, delete, deploy, restart, or stop operations can change infrastructure.

Mitigation: Run these operations only when requested and review generated code before execution.

## Reference(s):

- [Setup and usage reference](artifact/references/setup.md)
- [go-coolify project](https://github.com/psyb0t/go-coolify)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-coolify)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
