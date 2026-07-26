## Description: <br>
Trust + memory layer for AI agents. Write a verifiable behavioral track record (decisions, hallucinations) for free, and check the risk/reputation of any agent or token before moving money - paid over x402 on Base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rladlas](https://clawhub.ai/user/rladlas) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent operators use WaybackClaw to register agents, log decisions and hallucinations, and check agent or token reputation before financial actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send selected agent activity to a remote permanent archive. <br>
Mitigation: Do not log secrets, private keys, wallet seeds, credentials, personal data, regulated data, or sensitive trading strategy details. <br>
Risk: Paid reads use x402 payments on Base. <br>
Mitigation: Verify live x402 payment challenges before paying and trust the returned payTo and token address over documented defaults. <br>
Risk: Webhook usage can send archive events to external destinations. <br>
Mitigation: Use webhook destinations you control or trust. <br>


## Reference(s): <br>
- [WaybackClaw homepage](https://www.waybackclaw.space) <br>
- [WaybackClaw API Reference](references/api-reference.md) <br>
- [x402 Payments ($WBC on Base)](references/x402-payments.md) <br>
- [ClawHub skill page](https://clawhub.ai/rladlas/skills/waybackclaw) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls, JSON] <br>
**Output Format:** [Markdown with inline bash commands and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may include remote API calls, x402 payment headers, and agent-token configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
