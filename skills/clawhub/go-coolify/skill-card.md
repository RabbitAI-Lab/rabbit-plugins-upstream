## Description:

Writes Go code with go-coolify (package coolify, github.com/psyb0t/go-coolify), an unofficial generated client for the Coolify API covering applications, deployments, databases, services, projects, servers and teams. Use when Go code calls the Coolify API or already imports github.com/psyb0t/go-coolify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go code that reads or changes Coolify applications, deployments, databases, services, projects, servers, and teams through the go-coolify client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A misconfigured Coolify URL could send the bearer token to an unintended host.

Mitigation: Verify the HTTPS instance URL and use a narrowly scoped token; keep credentials out of source control and logs.

Risk: The generated Go dependency may include code that was not reviewed with this skill release.

Mitigation: Review and pin a trusted dependency version before production use.

Risk: Create, update, delete, deploy, restart, and stop operations change Coolify infrastructure.

Mitigation: Make these changes only when explicitly requested, and test examples locally first.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-coolify source repository](https://github.com/psyb0t/go-coolify)
- [go-coolify package documentation](https://pkg.go.dev/github.com/psyb0t/go-coolify)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-coolify)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Shell commands]

**Output Format:** [Go code and Markdown guidance with inline code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.8.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
