## Description:

PlanetScale CLI (pscale) command reference and workflows for authentication, organizations, databases, branches, maintenance, metrics, insights, SQL, deploy requests, backups, audit logs, service tokens, passwords, Cloudflare D1 imports, and automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database operators use this skill to get PlanetScale CLI command guidance, structured workflows, and shell automation for administering PlanetScale databases and related operational resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill covers broad PlanetScale administration workflows, including production-affecting deploys and deletes.

Mitigation: Install it only for agents intended to administer PlanetScale and confirm PlanetScale intent before routing database or authentication requests to it.

Risk: Deploys, deletes, demotions, credential changes, organization-member changes, and --force usage can alter production state or access.

Mitigation: Require explicit human approval for those actions, use tightly scoped PlanetScale credentials, and verify state before and after execution.

## Reference(s):

- [PlanetScale CLI documentation](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI GitHub repository](https://github.com/planetscale/cli)
- [PlanetScale community discussions](https://github.com/planetscale/discussion)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks and JSON-oriented command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to run pscale and bundled bash scripts; command execution should use scoped credentials and human approval for production-affecting actions.]

## Skill Version(s):

1.0.19 (source: server release evidence and artifact VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
