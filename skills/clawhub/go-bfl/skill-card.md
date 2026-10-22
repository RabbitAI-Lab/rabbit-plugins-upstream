## Description:

Helps developers write Go code using the unofficial go-bfl client to submit Black Forest Labs FLUX image and video tasks, poll results, check credits, and manage fine-tunes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to build Go integrations with the FLUX API, including image and video generation, result polling, credit checks, and fine-tune management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials or signed result URLs may be exposed or sent to an untrusted host.

Mitigation: Keep BFL_API_KEY out of logs and validate HTTPS and the provider host before following polling URLs.

Risk: Generation requests can incur charges, including duplicate charges from retries.

Mitigation: Submit only requested tasks and avoid automatic retries when a paid request's outcome is uncertain.

Risk: Deleting a fine-tune changes account state.

Mitigation: Run fine-tune deletion only when the user explicitly requests it.

## Reference(s):

- [go-bfl setup and API reference](references/setup.md)
- [go-bfl Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-bfl)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
