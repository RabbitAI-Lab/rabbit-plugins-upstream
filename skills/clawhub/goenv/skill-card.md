## Description:

Guides Go developers in using goenv to distinguish development from production by reading the ENV variable, treating only the exact value dev as development.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add a small prod/dev environment switch to their applications or understand existing goenv calls. It provides installation guidance, examples, and the exact ENV matching behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unset or unexpected ENV value selects production behavior instead of development behavior.

Mitigation: Confirm the application needs exact ENV=dev matching before adopting the library; test intended environment values.

Risk: Installation adds a third-party Go module to the project.

Mitigation: Review the dependency and its version before running go get.

## Reference(s):

- [Goenv setup and reference](references/setup.md)
- [Goenv library homepage](https://github.com/psyb0t/goenv)
- [Goenv ClawHub release](https://clawhub.ai/psyb0t/skills/goenv)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
