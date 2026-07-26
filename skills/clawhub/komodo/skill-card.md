## Description: <br>
Manage Komodo infrastructure including servers, Docker deployments, stacks, builds, and procedures via the Komodo Core API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[weird-aftertaste](https://clawhub.ai/user/weird-aftertaste) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to inspect and administer Komodo environments, including server status, container deployments, stacks, builds, procedures, logs, and direct API operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change or delete live Komodo-managed services, including deploy, stop, restart, delete, build, and procedure actions. <br>
Mitigation: Use least-privilege, environment-scoped API keys and require explicit human approval before actions that alter live services. <br>
Risk: Stack creation can include compose and environment file contents, which may expose secrets if raw secret-filled files are supplied. <br>
Mitigation: Review compose and env files before use, avoid uploading raw secret-filled env files unless intended, and scope credentials to the target environment. <br>


## Reference(s): <br>
- [Komodo API Documentation](https://komo.do/docs) <br>
- [ClawHub Skill Page](https://clawhub.ai/weird-aftertaste/skills/komodo) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown guidance with shell commands and CLI/API output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires KOMODO_ADDRESS, KOMODO_API_KEY, and KOMODO_API_SECRET environment variables.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
