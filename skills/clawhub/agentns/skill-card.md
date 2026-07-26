## Description: <br>
Register and manage ICANN domains for AI agents with wallet authentication, USDC payments on Base or Solana, and DNS management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vibrant](https://clawhub.ai/user/vibrant) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to check domain availability, register ICANN domains, manage registrant profiles, and administer DNS records for agent or project domains. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create wallet files and use wallets to spend USDC on domain registrations. <br>
Mitigation: Use a dedicated low-balance wallet, protect wallet files, pin and review the external client package, and require confirmation before wallet creation, payment, or registration. <br>
Risk: The skill can change live DNS records and nameservers. <br>
Mitigation: Require confirmation before DNS edits or nameserver changes and keep DNS backups so changes can be rolled back. <br>


## Reference(s): <br>
- [AgentNS homepage](https://agentns.xyz) <br>
- [agentns-client on PyPI](https://pypi.org/project/agentns-client/) <br>
- [AgentNS API docs](https://agentns.xyz/docs) <br>
- [ClawHub skill page](https://clawhub.ai/vibrant/skills/agentns) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with Python and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes domain registration, wallet setup, DNS management, nameserver, registrant profile, and error-handling examples.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
