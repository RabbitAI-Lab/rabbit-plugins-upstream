## Description: <br>
Openclaw provides secure key management guidance for AI agents handling private keys, API secrets, wallet credentials, delegated access, and agent-controlled funds. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zscole](https://clawhub.ai/user/zscole) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use Openclaw to design agents that can handle secrets, wallet credentials, and delegated spending with storage, validation, sanitization, session-key, and confirmation patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents handling private keys, API secrets, wallet credentials, or delegated spending can expose credentials or authorize unwanted transactions if access is too broad. <br>
Mitigation: Use dedicated vaults, avoid raw private key storage, issue short-lived session keys, and apply tight scope, value, and time limits. <br>
Risk: Prompt injection or unsafe outputs can attempt to reveal secrets or manipulate wallet operations. <br>
Mitigation: Validate inputs before wallet operations, sanitize all outputs for secret patterns, isolate wallet execution from conversation context, and require confirmation for high-value actions. <br>
Risk: Risky operational examples can weaken production controls if copied without review. <br>
Mitigation: Require an audited exception process, documented rollback plan, and human review before using hook bypasses, open delegations, or similar patterns in production. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zscole/skills/bagman) <br>
- [Secure Storage Patterns for Agent Secrets](references/secure-storage.md) <br>
- [Session Keys for Agent Wallet Access](references/session-keys.md) <br>
- [Leak Prevention for Agent Secrets](references/leak-prevention.md) <br>
- [Prompt Injection Defense for Agent Key Operations](references/prompt-injection-defense.md) <br>
- [Delegation Framework Integration (EIP-7710)](references/delegation-framework.md) <br>
- [EIP-7710 Specification](https://eips.ethereum.org/EIPS/eip-7710) <br>
- [MetaMask Delegation Framework](https://github.com/MetaMask/delegation-framework) <br>
- [MetaMask Smart Accounts Kit](https://docs.metamask.io/smart-accounts-kit) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline code and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; examples should be reviewed and adapted before production use.] <br>

## Skill Version(s): <br>
2.1.0 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
