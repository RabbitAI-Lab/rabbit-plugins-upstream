## Description: <br>
Deploy, resume, verify, destroy, and locally wire a production Dirextalk message server on AWS for local agent runtimes supported by dirextalk-connect. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yananli199307-dev](https://clawhub.ai/user/yananli199307-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to deploy and operate a Dirextalk message server on AWS, then connect supported local agent runtimes through dirextalk-connect and MCP. It also guides verification, updates, credential refresh, reset, and teardown. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create billable AWS resources that continue billing until removed. <br>
Mitigation: Require explicit deployment confirmation, review the generated cost estimate, and keep the destroy path and AWS Billing Console review visible to the operator. <br>
Risk: The deployment stores live Dirextalk and Matrix service tokens under the user's home directory. <br>
Mitigation: Restrict access to `~/.dirextalk/nodes/<service_id>/`, avoid printing or committing secrets, and rotate or delete credentials if local files may have been exposed. <br>
Risk: The local bridge can install npm packages and run a persistent service-scoped daemon. <br>
Mitigation: Review generated files before use, prefer service-scoped installation, and verify daemon status and logs before treating deployment as complete. <br>


## Reference(s): <br>
- [Dirextalk Deployer Homepage](https://github.com/YingSuiAI/dirextalk-deployer) <br>
- [ClawHub Skill Page](https://clawhub.ai/yananli199307-dev/skills/dirextalk-deployer) <br>
- [Agent Targets](references/agent-targets.md) <br>
- [Architecture](references/architecture.md) <br>
- [State Machine](references/state-machine.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration paths, and lifecycle status reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent-facing deployment, verification, local runtime wiring, update, reset, and destroy guidance; may reference generated files under the user's Dirextalk service directory.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
