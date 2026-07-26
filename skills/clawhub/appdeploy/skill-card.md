## Description: <br>
AppDeploy helps agents deploy or publish web apps with backend APIs, database, file storage, AI operations, authentication, realtime, and cron jobs to a public URL via HTTP API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[avimak](https://clawhub.ai/user/avimak) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and coding agents use AppDeploy to prepare deployment instructions, submit app files to AppDeploy, check deployment status, and manage deployed web apps with public URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AppDeploy sends app files to an external hosting service for public deployment. <br>
Mitigation: Install and use it only when public deployment through AppDeploy is intended, and review which files will be sent before deploying. <br>
Risk: Source snapshots or deployment files could include secrets or private credentials. <br>
Mitigation: Keep secrets out of source snapshots, keep .appdeploy private, and ensure .appdeploy is gitignored. <br>
Risk: Updating or deleting an existing app can overwrite or remove a public deployment. <br>
Mitigation: Require explicit confirmation before overwriting or deleting an existing app. <br>


## Reference(s): <br>
- [AppDeploy on ClawHub](https://clawhub.ai/avimak/skills/appdeploy) <br>
- [AppDeploy publisher profile](https://clawhub.ai/user/avimak) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Text] <br>
**Output Format:** [Markdown guidance with curl commands, JSON-RPC payloads, app file content, and deployment status text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create, update, inspect, or delete public app deployments when the corresponding tool workflow is used.] <br>

## Skill Version(s): <br>
1.0.7 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
