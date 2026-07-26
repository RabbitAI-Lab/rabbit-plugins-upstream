## Description: <br>
Guides the agent in Openclast/Openclaw wallet usage, approvals, and safety rules when users ask about wallet setup, balances, transactions, approvals, or key export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fabriziogianni7](https://clawhub.ai/user/fabriziogianni7) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to guide Openclast/Openclaw wallet setup, balance checks, transaction preparation, approvals, and key-export handling with explicit safety checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet transactions or contract operations can move assets if recipient, chain, amount, contract, or approval scope is wrong. <br>
Mitigation: Keep approval mode enabled and require the user to verify transaction details before broadcasting. <br>
Risk: Private-key export can expose wallet credentials. <br>
Mitigation: Avoid key export unless necessary, require explicit confirmation, and use host safety gates when available. <br>
Risk: The skill relies on separate Openclast wallet CLI or host wallet tools for actual wallet actions. <br>
Mitigation: Install and use it only where those tools are trusted, configured, and reviewed for the target environment. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/fabriziogianni7/skills/openclast-wallet) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline CLI commands and configuration field names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Instruction-only wallet guidance; no keys or transactions are produced by the skill itself.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
