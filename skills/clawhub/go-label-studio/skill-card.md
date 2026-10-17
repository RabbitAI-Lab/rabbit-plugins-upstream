## Description:

Guides Go developers in using the unofficial Label Studio client to work with projects, tasks, annotations, predictions, imports, exports, storage, webhooks, and administration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate the unofficial Label Studio client into applications that read or manage Label Studio resources. It explains authentication, API responses, and safe verification of client code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An API key could be exposed in source code or logs.

Mitigation: Load LABEL_STUDIO_API_KEY from the environment; never hardcode, commit, or log it.

Risk: Client requests could send credentials or task data to an unintended server.

Mitigation: Confirm LABEL_STUDIO_URL points to the intended installation and use HTTPS for remote servers.

Risk: Create, update, delete, webhook, storage, or user-admin calls can change server data.

Mitigation: Review actions and their targets before running them against a real server; use local tests to verify client wiring.

## Reference(s):

- [go-label-studio on ClawHub](https://clawhub.ai/psyb0t/skills/go-label-studio)
- [Go client homepage](https://github.com/psyb0t/go-label-studio)
- [Setup and reference](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for Go projects using a user-selected Label Studio server.]

## Skill Version(s):

0.1.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
