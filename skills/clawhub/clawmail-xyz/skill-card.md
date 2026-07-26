## Description: <br>
Email service for AI agents with wallet authentication and crypto payments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[patrickshuff](https://clawhub.ai/user/patrickshuff) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use ClawMail to give AI agents email addresses, wallet-based login, and MCP tools for mailbox management. The skill supports checking address availability, authenticating with wallet signatures, listing messages, reading messages, and deleting messages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet signatures and USDC payment prompts can authorize account access or charges if approved without review. <br>
Mitigation: Use a dedicated wallet where practical and require explicit review of wallet signature and USDC payment prompts before approval. <br>
Risk: Session tokens can expose mailbox access if shared with logs, prompts, or other tools. <br>
Mitigation: Keep JWT tokens private and avoid storing them in shared transcripts, logs, or configuration files. <br>
Risk: Mailbox deletion actions can permanently remove agent email messages. <br>
Mitigation: Require explicit approval before allowing an agent to delete mailbox messages. <br>


## Reference(s): <br>
- [ClawMail website](https://clawmail.xyz) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes MCP mailbox operations and REST API endpoint guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
