## Description: <br>
DACH compliance layer for x402 agents: Impressum, DSGVO, BFSG, cookie banner, and Preisangaben checks via x402 on Base USDC for German, Austrian, and Swiss URLs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[marketingkioldenburg](https://clawhub.ai/user/marketingkioldenburg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to call paid DACH website compliance checks for German, Austrian, and Swiss URLs. It helps agents request heuristic signals for imprint, privacy, accessibility, cookie banner, pricing, cancellation, URL preflight, agent-readiness, site-watch, and JSON repair workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends target URLs to an external service. <br>
Mitigation: Confirm the service URL and only submit URLs that are appropriate to share with the external provider. <br>
Risk: Paid endpoints require explicit x402/Base USDC payments. <br>
Mitigation: Confirm the quoted amount, payment address, network, and transaction before using an agent wallet. <br>
Risk: Compliance outputs are heuristic signals and are not legal advice. <br>
Mitigation: Use the results as screening inputs and consult qualified legal counsel for legal conclusions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/marketingkioldenburg/skills/dach-x402-compliance) <br>
- [Service homepage](https://agent.kihustle.tech) <br>
- [Service catalog](https://agent.kihustle.tech/promo/catalog.json) <br>
- [Payment documentation](https://agent.kihustle.tech/docs/how-to-pay) <br>
- [Agent discovery index](https://agent.kihustle.tech/llms.txt) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, JSON, API calls] <br>
**Output Format:** [Markdown guidance with curl examples and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Paid endpoints require x402/Base USDC payment before result retrieval; compliance results are heuristic signals and not legal advice.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
