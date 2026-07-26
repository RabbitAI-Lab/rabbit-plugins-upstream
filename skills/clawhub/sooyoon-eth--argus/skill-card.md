## Description: <br>
Argus Intelligence helps agents query an ARGUS API for onchain risk analysis, AML and compliance checks, prompt-injection screening, social verification, and webhook alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sooyoon-eth](https://clawhub.ai/user/sooyoon-eth) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and AI-agent operators use this skill to request blockchain intelligence, address or token risk checks, prompt-security screening, social verification, and webhook-based alerts from the configured ARGUS service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected blockchain addresses, prompts, usernames, agent IDs, webhook URLs, and payment proofs or tokens may be sent to the configured ARGUS service. <br>
Mitigation: Use the documented HTTPS endpoint, avoid sending private keys or seed phrases, and keep Stripe or payment tokens out of shared logs. <br>
Risk: Paid endpoints and webhook registration may create costs or persistent callbacks. <br>
Mitigation: Require explicit approval before paid requests or webhook registration, and track active webhooks for removal when no longer needed. <br>
Risk: Risk and compliance responses may be incomplete or unsuitable as the sole basis for enforcement decisions. <br>
Mitigation: Treat ARGUS responses as advisory and review high-impact recommendations before acting on them. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/sooyoon-eth/argus) <br>
- [Publisher profile](https://clawhub.ai/user/sooyoon-eth) <br>
- [Failsafe Security](https://getfailsafe.com) <br>
- [ARGUS capabilities](https://argus.getfailsafe.com/api/v1/capabilities) <br>
- [ARGUS Agent Card](https://argus.getfailsafe.com/.well-known/agent.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with curl examples and JSON API response descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ARGUS_ENDPOINT and curl; paid requests may require an approved Stripe token or x402 payment proof.] <br>

## Skill Version(s): <br>
1.9.3 (source: server release metadata; artifact frontmatter, package.json, skill.json, and README.md report 1.9.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
