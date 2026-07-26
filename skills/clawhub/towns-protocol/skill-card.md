## Description: <br>
Helps developers build Towns Protocol bots with SDK setup, event handlers, messaging, interactive components, blockchain operations, debugging, and deployment guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andreyz](https://clawhub.ai/user/andreyz) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to create, test, debug, and deploy Towns Protocol bots that handle slash commands, messages, reactions, interactive forms, and Base network transactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bot credentials, JWT secrets, RPC keys, database URLs, and funded wallets can be exposed if copied into source control or public logs. <br>
Mitigation: Store secrets in environment variables or a secret manager, keep funded wallets limited, and avoid logging message bodies or wallet identifiers outside local debugging. <br>
Risk: Blockchain workflows can grant access or value based on an unconfirmed transaction hash. <br>
Mitigation: Verify transaction receipts on-chain and require receipt.status === 'success' before granting access or treating payment as complete. <br>
Risk: Webhook tunnels and broad bot permissions can expose development services or excessive chat access. <br>
Mitigation: Use tunnels only temporarily, configure the minimum required message forwarding mode, and limit bot permissions to the channels and actions needed. <br>


## Reference(s): <br>
- [Towns Protocol skill page](https://clawhub.ai/andreyz/skills/towns-protocol) <br>
- [Towns Developer Portal](https://app.towns.com/developer) <br>
- [Towns bot documentation](https://docs.towns.com/build/bots) <br>
- [@towns-protocol/bot SDK](https://www.npmjs.com/package/@towns-protocol/bot) <br>
- [Messaging API](references/MESSAGING.md) <br>
- [Blockchain Operations](references/BLOCKCHAIN.md) <br>
- [Interactive Components](references/INTERACTIVE.md) <br>
- [Deployment](references/DEPLOYMENT.md) <br>
- [Debugging](references/DEBUGGING.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with TypeScript, shell, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only output; does not execute commands or call services by itself.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
