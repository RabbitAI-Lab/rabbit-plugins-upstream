## Description:

PlanetScale CLI (pscale) command reference and workflows for authentication, organizations, databases, branches, deploy requests, SQL, metrics, diagnostics, backups, credentials, Traffic Control, PgBouncers, Cloudflare D1 imports, and related automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database operators use this skill to plan and run PlanetScale CLI workflows, inspect command output, and execute bundled shell automation for branch, deploy-request, SQL, metrics, diagnostic, backup, credential, and organization administration tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-impact PlanetScale administration actions such as deploys, deletions, credential rotation, organization member changes, force flags, and production-impacting operations.

Mitigation: Install only where the agent is authorized to administer PlanetScale resources, require explicit user confirmation for these actions, and verify results after writes.

Risk: Broad trigger activation could expose administrative guidance in unrelated conversations.

Mitigation: Scope activation to PlanetScale and pscale tasks and avoid loading the skill for unrelated requests.

Risk: Service tokens and CLI authentication can grant access to production databases.

Mitigation: Prefer least-privilege service tokens, keep credentials in environment variables or approved secret stores, and avoid logging or committing credential material.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills)
- [PlanetScale CLI reference](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI GitHub repository](https://github.com/planetscale/cli)
- [PlanetScale community discussions](https://github.com/planetscale/discussion)
- [pscale branch command reference](pscale-branch/references/commands.md)
- [pscale deploy-request command reference](pscale-deploy-request/references/commands.md)
- [pscale sql command reference](pscale-sql/references/commands.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, code, configuration]

**Output Format:** [Markdown with inline bash code blocks, command examples, decision guidance, and shell scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the pscale CLI and jq for bundled automation scripts; optional PlanetScale service-token environment variables may be used for CI/CD authentication.]

## Skill Version(s):

1.0.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
