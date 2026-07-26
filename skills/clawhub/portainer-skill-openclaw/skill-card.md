## Description: <br>
Comprehensive management for Portainer CE environments and stacks, including environment listing, Docker Compose and Swarm stack management, and raw Docker API requests through Portainer. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leventsoft](https://clawhub.ai/user/leventsoft) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to administer Portainer CE environments from an OpenClaw agent, including checking environments and stacks, deploying or updating Compose stacks, removing stacks, and issuing Docker API requests through Portainer. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad Portainer and Docker administration capability. <br>
Mitigation: Install only when agent-based Portainer administration is intended, and use a least-privilege Portainer token. <br>
Risk: Deploy, update, prune, remove, and raw Docker API operations can interrupt services or delete resources. <br>
Mitigation: Avoid production targets unless confirmations, allowlists, and operational review are added before executing destructive or service-impacting actions. <br>
Risk: The security evidence reports an insecure TLS setup. <br>
Mitigation: Enable real TLS certificate verification before using the skill against sensitive or production Portainer instances. <br>


## Reference(s): <br>
- [Portainer](https://www.portainer.io/) <br>
- [ClawHub Skill Page](https://clawhub.ai/leventsoft/skills/portainer-skill-openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured JSON-like command output with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return Portainer and Docker API response data, stack details, status messages, or error messages.] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
