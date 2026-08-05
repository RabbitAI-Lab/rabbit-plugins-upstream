## Description: <br>
Self-custody Ethereum wallet for agents that runs locally as a Docker or Podman MCP stdio service, lets agents read wallet and DeFi context, preview transactions, park user-approved sends, and sign plaintext messages while keeping private keys in a local volume. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rustok](https://clawhub.ai/user/rustok) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to give an agent a local Ethereum wallet for wallet context, balance and DeFi position lookup, transaction preview, human-approved transaction execution, and plaintext message signing. It is appropriate only when the user understands self-custody wallet risk and intentionally grants the agent the configured wallet capabilities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates a real self-custody Ethereum wallet for an agent, and funds in that wallet can be lost. <br>
Mitigation: Use read-only or preview-only capabilities unless transaction execution or message signing is intentionally required, and fund the wallet only at an amount appropriate for the agent's trust level. <br>
Risk: Recovery phrases, approval PINs, and keyring passwords can be exposed if entered into an agent chat or agent-controlled shell. <br>
Mitigation: Keep wallet creation, console approval, recovery phrases, PINs, and keyring passwords in a separate user-controlled terminal and out of agent-visible context. <br>
Risk: Plaintext message signing is not gated by the separate console approval flow. <br>
Mitigation: Connect the wallet only to agents trusted to sign messages, and review message-signing requests with the same care as other wallet actions. <br>
Risk: An agent with shell or container access may bypass intended wallet interaction boundaries. <br>
Mitigation: Do not grant untrusted agents shell or docker exec access to the wallet container, and rely on capability scoping for normal MCP sessions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rustok/skills/rustok-wallet-tui) <br>
- [Rustok project homepage](https://github.com/rustok-org/mcp) <br>
- [Installation guide](https://github.com/rustok-org/mcp/blob/main/docs/INSTALL.md) <br>
- [Caveats and limitations](https://github.com/rustok-org/mcp/blob/main/docs/CAVEATS.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes self-custody wallet safety guidance, transaction preview and approval flow instructions, and capability-scoping recommendations.] <br>

## Skill Version(s): <br>
0.8.4 (source: artifact/SKILL.md frontmatter, artifact/claw.json, and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
