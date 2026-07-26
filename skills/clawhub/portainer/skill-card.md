## Description: <br>
Portainer controls Docker containers and stacks through the Portainer API, including listing status, starting, stopping, restarting, viewing logs, and redeploying stacks from git. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[asteinberger](https://clawhub.ai/user/asteinberger) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to let an agent inspect and manage Docker environments exposed through Portainer. It is suited for operational workflows such as checking service status, reviewing logs, restarting containers, and redeploying stacks when the Portainer token is appropriately scoped. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent live control over Portainer-managed infrastructure, including stop, restart, and redeploy actions. <br>
Mitigation: Use a least-privilege Portainer API token, prefer non-production or tightly scoped endpoints, and require explicit confirmation with exact stack, container, and endpoint names before disruptive actions. <br>
Risk: The skill depends on Portainer credentials stored in environment variables or a local .env file. <br>
Mitigation: Protect the credential file, avoid broad or shared tokens, and rotate the API token if it may have been exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/asteinberger/skills/portainer) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell command examples and plain-text command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, PORTAINER_URL, and PORTAINER_API_KEY; actions call the Portainer API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
