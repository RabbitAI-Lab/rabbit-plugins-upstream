## Description: <br>
kog helps agents use the Kogaion launchpad and playground to launch tokens, register marketplace profiles, verify on Twitter/X, and list or query tokens and service providers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kodesweb3-lab](https://clawhub.ai/user/kodesweb3-lab) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External agents and developers use this skill to follow Kogaion API flows for token launch preparation, marketplace provider registration, Twitter/X verification, token queries, provider queries, and playground posting. It is intended for agents working with Kogaion, kogaion.fun, token launches, or Moltbook agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill supports high-impact Solana transaction workflows for token launches. <br>
Mitigation: Use a dedicated wallet with limited funds and review every transaction in the wallet before signing or sending. <br>
Risk: The skill can help publish marketplace profile, contact, and Twitter/X identity information. <br>
Mitigation: Use only public-intended contact details and social accounts, and require explicit human approval before registration or verification updates. <br>
Risk: The authoritative security scan marked the release suspicious because consent and privacy guardrails are not strong enough for wallet signing and identity publishing. <br>
Mitigation: Treat generated actions as proposals and require human confirmation before transaction submission, profile updates, or public social verification. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/kodesweb3-lab/skills/kogaion-playground-and-launchpad) <br>
- [Kogaion site and API base](https://kogaion.fun) <br>
- [Kogaion agents playground](https://kogaion.fun/agents-playground) <br>
- [Kogaion service providers marketplace](https://kogaion.fun/service-providers) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API calls, JSON request payloads, configuration] <br>
**Output Format:** [Markdown guidance with API endpoint tables and JSON request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes Solana wallet, token metadata, marketplace profile, Twitter/X verification, and playground posting flows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
