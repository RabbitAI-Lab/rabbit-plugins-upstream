## Description:

PlanetScale CLI Skills provides command references, workflows, and automation for authenticated pscale operations across databases, branches, deploy requests, SQL, metrics, insights, backups, audit logs, credentials, and organization management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to plan and run PlanetScale administration through the pscale CLI, including branch workflows, production schema deploy requests, diagnostics, metrics, credential workflows, and related automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide powerful PlanetScale administration actions involving deploys, deletes, restores, credential rotation, organization membership, traffic control, and SQL writes.

Mitigation: Require explicit human approval before those actions, restating the exact organization, database, branch, target resource, and proposed command.

Risk: Credential and authentication workflows can expose service tokens, database passwords, API headers, or audit-log data if copied into logs or unapproved files.

Mitigation: Keep credentials in the user config, environment variables, or an approved secret manager, and avoid printing secrets or raw authentication exports in chat or logs.

Risk: Force, unblock, destructive SQL, traffic-control enforcement, and production deploy actions can change application behavior or availability.

Mitigation: Prefer read-only inspection first, preserve current state, confirm rollback or recovery paths, and run write commands only after approval for the exact target and impact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills)
- [PlanetScale CLI documentation](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI repository](https://github.com/planetscale/cli)
- [PlanetScale community discussions](https://github.com/planetscale/discussion)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands, scripts, and structured CLI-output interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated pscale CLI; bundled automation scripts also require jq. Optional service-token environment variables are PLANETSCALE_SERVICE_TOKEN_ID and PLANETSCALE_SERVICE_TOKEN.]

## Skill Version(s):

1.0.17 (source: evidence release.version and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
