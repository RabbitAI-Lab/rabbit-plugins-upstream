## Description: <br>
The Economic OS for OpenClaw. Autonomous USDC wallets on Base L2 via x402. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[horizonflowhq-ai](https://clawhub.ai/user/horizonflowhq-ai) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and agent users use AgentPayy to give an OpenClaw agent wallet onboarding, Base L2 USDC balance checks, paid x402 request handling, and agent-to-agent payment workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent real spending authority for crypto micropayments. <br>
Mitigation: Use low-balance wallets and require explicit approval or strict budget and merchant limits before funding or executing paid requests. <br>
Risk: External SDK and payment flows can affect wallet security and transaction integrity. <br>
Mitigation: Review the external SDK package before installation and monitor wallet transactions after enabling the skill. <br>
Risk: Marketplace and referral behavior may influence tool recommendations. <br>
Mitigation: Require disclosure and user approval for paid recommendations, referrals, and marketplace-driven hiring decisions. <br>


## Reference(s): <br>
- [AgentPayy ClawHub Skill Page](https://clawhub.ai/horizonflowhq-ai/skills/agentpayy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with Python code examples and setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to install Python packages and interact with wallet, payment, marketplace, and referral workflows.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
