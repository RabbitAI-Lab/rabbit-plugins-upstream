## Description: <br>
Helps an agent run pre-trade on-chain token diligence, including rug and honeypot checks, DEX liquidity and price review, whale transfer flows, and smart-money wallet activity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rccola990-cloud](https://clawhub.ai/user/rccola990-cloud) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agent operators use this skill before buying, swapping, recommending, or sizing a crypto token trade. It guides the agent to call disclosed on-chain diligence endpoints and review risk, liquidity, whale-flow, and wallet-activity signals before making a recommendation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends crypto token, ticker, and wallet identifiers to store.agentexchange.work. <br>
Mitigation: Confirm the user is comfortable sharing those identifiers with the third-party service before making calls. <br>
Risk: Paid x402 endpoint calls can spend USDC if an x402-enabled client automatically retries after HTTP 402 payment requirements. <br>
Mitigation: Use the free sample first, review prices shown in payment requirements, and monitor client spending controls before paid calls. <br>


## Reference(s): <br>
- [AgentExchange endpoint catalog](https://store.agentexchange.work) <br>
- [AgentExchange free sample endpoint](https://store.agentexchange.work/samples) <br>
- [ClawHub skill page](https://clawhub.ai/rccola990-cloud/skills/onchain-token-diligence) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands] <br>
**Output Format:** [Markdown with HTTP GET examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May involve x402 paid endpoint calls; use the free sample first and review payment prompts before paid calls.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
