## Description: <br>
Human-in-the-loop security layer. Intercepts high-risk commands and requires push notification approval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lucky-2968](https://clawhub.ai/user/lucky-2968) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to route shell command execution through a human approval workflow for higher-risk commands and to inspect pending approvals or audit logs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package claims to secure shell execution, but the submitted artifact does not include the tool implementation. <br>
Mitigation: Do not rely on it as a shell security layer until the publisher provides and documents the implementation. <br>
Risk: Install metadata fetches an unrelated npm package. <br>
Mitigation: Inspect the npm dependency and test only in a disposable environment with dedicated notification tokens. <br>
Risk: Adding the documented TOOLS.md rule would route all shell access through a tool that is not present in the artifact. <br>
Mitigation: Do not route all shell commands through this skill until the expected tools exist and behave as documented. <br>


## Reference(s): <br>
- [Clawshell 0.1.0 on ClawHub](https://clawhub.ai/lucky-2968/skills/clawshell-0-1-0) <br>
- [Pushover application setup](https://pushover.net/apps/build) <br>
- [Referenced npm package-lock.json package](https://registry.npmjs.org/package-lock.json/-/package-lock.json-1.0.0.tgz) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, text, configuration, guidance] <br>
**Output Format:** [Tool responses with command exit data, status text, audit-log summaries, and setup guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node and notification credentials for the claimed approval workflow.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter lists 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
