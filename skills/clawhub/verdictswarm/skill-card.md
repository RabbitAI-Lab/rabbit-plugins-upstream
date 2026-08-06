## Description: <br>
Check token risk before trading on Solana or Base. Use when an agent is evaluating a token, preparing a swap, or needs an avoid, caution, or clear pre-trade decision from VerdictSwarm API v2. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vswarm-ai](https://clawhub.ai/user/vswarm-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use VerdictSwarm as a pre-trade risk gate for Solana or Base tokens before preparing a swap or other money-moving action. The skill returns guidance to avoid, use caution, or proceed when no blocking risk is found by the scan. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Token details are sent to the VerdictSwarm API for analysis. <br>
Mitigation: Use the skill only when sharing the token address and chain with VerdictSwarm is acceptable for the workflow. <br>
Risk: Returned API keys are secrets and could be exposed through chat, logs, source control, or shared memory. <br>
Mitigation: Store the key in VS_API_KEY or an approved secret store and avoid printing it in user-visible or persistent outputs. <br>
Risk: A clear verdict can inform a trade decision but does not prove that a token is safe or profitable. <br>
Mitigation: Present clear as no blocking risk found by the scan, and keep insufficient data, low confidence, degraded results, and failed signals visible to the user. <br>
Risk: x402 overflow requests may spend USDC when free quota is exhausted. <br>
Mitigation: Require explicit user approval before paying an x402 challenge or retrying a paid request. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vswarm-ai/skills/verdictswarm) <br>
- [VerdictSwarm product](https://www.vswarm.io) <br>
- [VerdictSwarm API docs](https://www.vswarm.io/docs/api) <br>
- [Live API info](https://api.vswarm.io/v2/verdict/info) <br>
- [VerdictSwarm MCP listing](https://smithery.ai/servers/sentien-labs/verdictswarm-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require curl and a VerdictSwarm API key for live API calls.] <br>

## Skill Version(s): <br>
3.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
