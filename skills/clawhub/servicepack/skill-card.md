## Description:

Guides developers in building and running concurrent Go services from the servicepack clone-and-own template, with dependency ordering, retries, readiness checks, and graceful shutdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building Go applications use this skill to scaffold and configure multiple cooperating services in one binary or separate microservices, and to test their startup, retry, and shutdown behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The make own command replaces project files and reinitializes Git history.

Mitigation: Run make own only in a fresh clone and review the proposed changes before proceeding.

Risk: Services added by users may access networks, databases, or secrets.

Mitigation: Review each added service's network access, database use, and secret handling before deployment.

## Reference(s):

- [servicepack on ClawHub](https://clawhub.ai/psyb0t/skills/servicepack)
- [servicepack project homepage](https://github.com/psyb0t/servicepack)
- [Setup guide](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Docker for the supported build and test commands.]

## Skill Version(s):

1.10.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
