## Description:

Goenv helps agents add or explain a small Go prod/dev environment switch based on the ENV variable, where only the exact value "dev" returns dev and all other values return prod.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when they want an agent to help install, import, or apply github.com/psyb0t/goenv in a Go program for a simple prod/dev branch. It is suited to projects that accept a fixed ENV variable and two environment states.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the library may add an external Go dependency and run go get, which can fetch from the configured Go module proxy.

Mitigation: Confirm the dependency is desired, review the module source through normal project dependency controls, and pin it through Go modules before deployment.

Risk: Only ENV=dev is treated as dev; unset, misspelled, uppercase, or other values default to prod.

Mitigation: Document the exact accepted ENV value and test launch configuration for each environment that relies on dev behavior.

## Reference(s):

- [goenv setup and reference](references/setup.md)
- [goenv GitHub repository](https://github.com/psyb0t/goenv)
- [Goenv on ClawHub](https://clawhub.ai/psyb0t/skills/goenv)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Go and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May suggest go get, Go imports, ENV configuration, and small source edits in the user's current Go project.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
