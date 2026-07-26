## Description: <br>
Shop autonomously on Amazon via Moltpho - search products, manage credit, and purchase items using mUSD on Base mainnet. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unifiedh](https://clawhub.ai/user/unifiedh) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an agent search Amazon, manage Moltpho credit, create quotes, place orders, track order state, and handle support workflows through Moltpho. <br>

### Deployment Geography for Use: <br>
United States <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place real Amazon orders and spend stored Moltpho credit without a mandatory final confirmation by default. <br>
Mitigation: Enable confirmation-required mode, disable proactive purchasing unless needed, and set strict per-order and daily caps before use. <br>
Risk: Broad inferred conversation signals may trigger proactive purchasing. <br>
Mitigation: Configure denylists or allowlists and keep proactive purchasing disabled unless that behavior is explicitly desired. <br>
Risk: The local credentials file can authorize Moltpho API actions. <br>
Mitigation: Protect the credentials file and use the Moltpho portal for payment and shipping setup where possible. <br>


## Reference(s): <br>
- [Moltpho ClawHub Skill Page](https://clawhub.ai/unifiedh/skills/moltpho) <br>
- [Moltpho API Reference](artifact/references/API.md) <br>
- [Moltpho Purchasing Policies](artifact/references/POLICIES.md) <br>
- [Moltpho API](https://api.moltpho.com) <br>
- [Moltpho Portal](https://portal.moltpho.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, API calls, Configuration] <br>
**Output Format:** [Natural-language responses with API-backed JSON data, purchase status, support-ticket details, and portal URLs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires HTTP and browser access; may store local credential JSON for Moltpho API authentication.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
