## Description: <br>
Provides PlanetScale CLI command references, decision guidance, and bash workflows for managing databases, branches, deploy requests, SQL queries, diagnostics, imports, backups, passwords, service tokens, and organizations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vince-winkintel](https://clawhub.ai/user/vince-winkintel) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and database engineers use this skill to operate PlanetScale resources through the pscale CLI, including branch workflows, deploy requests, read-only diagnostics, non-interactive SQL, D1 imports, and CI/CD automation. It is intended for users who already have authorized PlanetScale access and need concise command guidance or shell workflow generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide real PlanetScale database, credential, and production deployment actions. <br>
Mitigation: Require explicit confirmation of the organization, database, branch, command, and exact SQL before any delete, deploy, revert, promote, password or token change, write-capable SQL, connection kill, resize, routing, throttler, or import action. <br>
Risk: Overly broad triggers or incomplete guardrails could lead an agent to propose higher-impact operations than the user intended. <br>
Mitigation: Prefer read-only commands, JSON inspection, dry runs, and deploy-request review flows by default; escalate to write or production commands only after the requested operation and target are clear. <br>
Risk: PlanetScale service tokens and API credentials may be needed for CI/CD or automation workflows. <br>
Mitigation: Keep credentials in environment variables or a secret manager, avoid printing or logging secret-bearing values, and pass secrets only to verified PlanetScale CLI/API targets. <br>


## Reference(s): <br>
- [PlanetScale CLI reference](https://planetscale.com/docs/reference/planetscale-cli) <br>
- [PlanetScale CLI GitHub repository](https://github.com/planetscale/cli) <br>
- [PlanetScale community discussions](https://github.com/planetscale/discussion) <br>
- [ClawHub skill page](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills) <br>
- [Root skill definition](artifact/SKILL.md) <br>
- [Release version notes](artifact/VERSION) <br>
- [pscale auth command reference](artifact/pscale-auth/references/commands.md) <br>
- [pscale branch command reference](artifact/pscale-branch/references/commands.md) <br>
- [pscale deploy-request command reference](artifact/pscale-deploy-request/references/commands.md) <br>
- [pscale sql command reference](artifact/pscale-sql/references/commands.md) <br>
- [pscale inspect command reference](artifact/pscale-inspect/references/commands.md) <br>
- [pscale insights command reference](artifact/pscale-insights/references/commands.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and occasional JSON-oriented parsing instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose pscale and jq commands or bundled bash scripts; execution requires local PlanetScale CLI authentication and user-approved targets.] <br>

## Skill Version(s): <br>
1.0.9 (source: evidence.release.version and artifact/VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
