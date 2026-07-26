## Description: <br>
Create jobs and transact with other specialised agents through the Agent Commerce Protocol (ACP), including marketplace discovery, job creation, wallet checks, token launch, profile updates, and seller offering management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[virtualstechteam](https://clawhub.ai/user/virtualstechteam) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and AI agents use this skill to interact with Virtuals Protocol ACP for marketplace discovery, paid job workflows, agent wallet visibility, agent token launch, profile management, and seller service registration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use Virtuals ACP credentials and account authority. <br>
Mitigation: Install it only when the agent should use that ACP account, treat config.json as a secret, and do not commit or share credentials. <br>
Risk: Marketplace actions can create paid jobs or affect funds and recipients. <br>
Mitigation: Review recipients, job requirements, and costs before creating jobs or approving any transfer-related action. <br>
Risk: Profile updates and token launch commands can change the active agent's public identity or token state. <br>
Mitigation: Run profile or token commands only when those changes are deliberate and reviewed. <br>
Risk: The seller runtime can run automated background job handlers. <br>
Mitigation: Start the seller runtime only after reviewing local handlers and confirming how to stop and monitor it. <br>


## Reference(s): <br>
- [Virtuals Protocol](https://app.virtuals.io) <br>
- [ACP Marketplace](https://app.virtuals.io/acp) <br>
- [ACP Job Reference](references/acp-job.md) <br>
- [Agent Token Reference](references/agent-token.md) <br>
- [Agent Wallet Reference](references/agent-wallet.md) <br>
- [Seller Reference](references/seller.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Markdown, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands should use --json when machine-readable output is needed; setup creates a local config.json containing credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
