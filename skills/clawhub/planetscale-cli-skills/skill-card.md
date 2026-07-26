## Description: <br>
Comprehensive PlanetScale CLI command reference and workflows for database, branch, deploy request, SQL, D1 import, backup, credential, service token, and organization operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vince-winkintel](https://clawhub.ai/user/vince-winkintel) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and database operators use this skill to plan and run PlanetScale CLI workflows, including schema branch management, deploy requests, non-interactive SQL queries, Cloudflare D1 imports, backups, and credential administration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help run live PlanetScale CLI commands against authenticated databases, branches, deploy requests, backups, SQL endpoints, and credentials. <br>
Mitigation: Verify the organization, database, branch, deploy request, backup ID, SQL statement, and credential target before execution, and require explicit user confirmation for destructive or write-capable commands. <br>
Risk: Deploy, revert, promote, import, routing, MoveTables, delete, and write SQL operations can change production data or database topology. <br>
Mitigation: Prefer dry runs, diffs, linting, JSON status checks, and deploy-request review workflows before live execution; show the exact command and target before proceeding. <br>
Risk: Service tokens and database passwords may be exposed if commands, logs, or shell history include secrets. <br>
Mitigation: Use environment variables or secret managers for PlanetScale credentials, avoid printing tokens, and rotate or delete temporary credentials after use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills) <br>
- [PlanetScale CLI Documentation](https://planetscale.com/docs/reference/planetscale-cli) <br>
- [PlanetScale CLI GitHub Repository](https://github.com/planetscale/cli) <br>
- [PlanetScale Community Discussions](https://github.com/planetscale/discussion) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline bash commands and concise operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include command review notes, JSON-output parsing guidance, and target confirmation prompts before live operations.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata and VERSION file) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
