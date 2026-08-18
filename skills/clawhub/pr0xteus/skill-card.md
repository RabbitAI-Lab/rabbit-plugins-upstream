## Description:

pr0xteus helps trusted self-hosted workloads request and operate operator-approved WireGuard-backed SOCKS5 exits through a private bearer-protected controller, including pool inspection, assignment replacement, and Go-client integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to give trusted services controlled, country-specific SOCKS5 egress through an operator-owned pr0xteus controller without exposing an open proxy. It is also used to inspect pools and cells, replace failed assignments, and follow documented setup or Go-client integration paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Control tokens and returned SOCKS5 URLs are bearer capabilities that could grant access if exposed.

Mitigation: Read tokens from trusted environment or secret storage, keep PR0XTEUS_API_TOKEN and SOCKS5 URLs out of logs and public artifacts, and unset temporary shell variables after use.

Risk: Allocating or deleting cells can consume provider capacity or disrupt the task's active egress path.

Mitigation: Request only operator-approved countries or pools for the user-named task, and delete only cells associated with user-requested cleanup for that allocation.

Risk: Setup commands download an installer and run Docker operations that affect local networking and configuration.

Mitigation: Inspect the downloaded installer before execution, use trusted private controller endpoints, pin released images unless explicitly using rolling behavior, and keep controller access protected.

Risk: Misconfiguration could turn private egress plumbing into an exposed proxy surface.

Mitigation: Keep the controller on loopback or another protected bind address, use operator-owned WireGuard material, and avoid untrusted callers or unapproved destinations.

## Reference(s):

- [pr0xteus setup](references/setup.md)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/pr0xteus)
- [Project homepage](https://github.com/psyb0t/pr0xteus)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown guidance with bash, curl, Docker, jq, YAML, and Go-client examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill provides operator-facing instructions and request examples; it does not expose an MCP endpoint or execute controller operations by itself.]

## Skill Version(s):

0.10.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
