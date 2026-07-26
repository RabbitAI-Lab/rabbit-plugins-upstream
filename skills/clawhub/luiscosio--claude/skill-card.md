## Description: <br>
Spin up, SSH into, run commands on, and tear down Linux servers from Claude, with payment by USDC over x402 or card. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luiscosio](https://clawhub.ai/user/luiscosio) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to browse, provision, operate, renew, and destroy real Linux VPS instances from Claude workflows. It is suited to deployment, hosting, command execution, diagnostics, and infrastructure management tasks where paid server provisioning is intentional. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can provision paid infrastructure and renew leases, which can create unintended spend. <br>
Mitigation: Use a dedicated limited wallet and set a low AGENTMETAL_MAX_USDC cap before allowing provisioning or renewal. <br>
Risk: The skill can run commands as root on managed servers and change firewall exposure. <br>
Mitigation: Require manual confirmation for root command execution, firewall changes, reboot, diagnostics, renewal, and destroy operations. <br>
Risk: Managed SSH keys, returned private keys, wallet keys, and AgentMetal API keys are sensitive credentials. <br>
Mitigation: Treat all returned private keys and environment variables as secrets, use dedicated limited credentials, and avoid exposing them in logs or shared transcripts. <br>


## Reference(s): <br>
- [AgentMetal API documentation for agents](https://api.agentmetal.dev/llms.txt) <br>
- [ClawHub skill page](https://clawhub.ai/luiscosio/skills/claude) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/luiscosio) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, Shell commands, API calls] <br>
**Output Format:** [Markdown with inline JSON and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include server identifiers, SSH connection details, command output, firewall settings, payment-related configuration, and secret-handling guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
