## Description:

Writes Go code with go-coolify, an unofficial generated client for the Coolify API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add Go code that calls a Coolify instance to inspect or manage applications, deployments, databases, services, projects, servers, and teams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan is partial and reports that a local path-like reference in SKILL.md could not be resolved, leaving evidence incomplete.

Mitigation: Review the unresolved reference and scan guidance before installing.

Risk: The Go client can make infrastructure-changing Coolify calls, including create, update, delete, deploy, restart, and stop operations.

Mitigation: Use changing operations only when requested, and confirm the target instance and resource before calling them.

Risk: Coolify API tokens are bearer credentials sent with requests.

Mitigation: Use HTTPS for remote instances, send the token only to the intended instance, and keep it out of source control and logs.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-coolify source repository](https://github.com/psyb0t/go-coolify)
- [go-coolify Go documentation](https://pkg.go.dev/github.com/psyb0t/go-coolify)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-coolify)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.10.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
