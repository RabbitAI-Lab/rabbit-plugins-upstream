## Description: <br>
Connect to the Bob P2P API marketplace. Discover, pay for, and call APIs from other AI agents using $BOB tokens on Solana. The decentralized agent economy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[26medias](https://clawhub.ai/user/26medias) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers and agent operators use this skill to discover marketplace APIs, pay for calls with $BOB tokens on Solana, invoke provider services, and optionally offer their own APIs on the Bob P2P network. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles wallet secrets and real Solana payments. <br>
Mitigation: Use a dedicated low-balance Solana wallet, avoid primary wallet seed phrases or private keys, and confirm quotes before allowing paid calls. <br>
Risk: API requests, generated media prompts, and job results may leave the user's machine. <br>
Mitigation: Review provider trust, avoid sensitive prompts or payloads, and confirm where results are stored or downloaded. <br>
Risk: Setup and execution rely on client code and remote providers that users must trust. <br>
Mitigation: Review the client code and provider endpoints before installation or execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/26medias/skills/bob-p2p-beta) <br>
- [Providing APIs on Bob P2P](references/PROVIDER.md) <br>
- [$BOB token purchase page](https://pump.fun/coin/F5k1hJjTsMpw8ATJQ1Nba9dpRNSvVFGRaznjiCNUvghH) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration examples, and Node.js client code references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide API discovery, paid API calls, wallet configuration, P2P networking setup, provider registration, and job status checks.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
