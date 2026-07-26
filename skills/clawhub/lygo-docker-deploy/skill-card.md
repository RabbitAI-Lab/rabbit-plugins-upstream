## Description: <br>
Deploy a sovereign LYGO Protocol Stack community node with Docker or Docker Compose, including a lygo-node image, local health API on port 8787, and optional worker scaling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to bring up a local LYGO Protocol Stack community node, verify the health, badge, and gossip endpoints, and optionally start horizontal worker processes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Deployment or publishing actions can affect local containers, registries, or remote services. <br>
Mitigation: Confirm the target, reason, command output, and authenticated account before approving deploy, registry push, or other sensitive actions. <br>
Risk: The node starts a local health API on port 8787 that could be unsafe if exposed publicly. <br>
Mitigation: Keep the service local unless TLS and explicit user approval are in place before public exposure. <br>


## Reference(s): <br>
- [LYGO Protocol Stack Repository](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [LYGO Protocol Stack Documentation](https://deepseekoracle.github.io/lygo-protocol-stack/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes Docker Compose and local API verification commands; public exposure, registry push, and cloud deployment require explicit user approval.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
