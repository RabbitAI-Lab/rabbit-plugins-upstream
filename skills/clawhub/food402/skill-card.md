## Description: <br>
Order food from TGO Yemek (Trendyol GO), Turkey's food delivery service, including restaurant browsing, menu review, address management, basket management, order history, and 3D Secure checkout. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rersozlu](https://clawhub.ai/user/rersozlu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users in Turkey use this skill to have an agent browse TGO Yemek restaurants and menus, manage delivery addresses and baskets, and guide checkout. It is intended for account-backed food ordering where the user remains responsible for confirming address, basket, total, and payment details. <br>

### Deployment Geography for Use: <br>
Turkey <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access a user's TGO account, saved delivery addresses, basket, order history, and saved-card checkout flow. <br>
Mitigation: Install only on a trusted single-user machine and use an account and payment profile appropriate for agent-assisted food ordering. <br>
Risk: Orders and payments can be submitted through saved-card and 3D Secure flows. <br>
Mitigation: Require user confirmation of the restaurant, delivery address, basket contents, total price, and selected card before placing an order. <br>
Risk: Authentication tokens and 3D Secure HTML are handled through temporary local files with limited safeguards. <br>
Mitigation: Clear cached tokens after use, keep temporary directories private, and open 3D Secure content only when the user expects the payment challenge. <br>
Risk: Optional Google Places review lookup requires an additional API key. <br>
Mitigation: Do not configure GOOGLE_PLACES_API_KEY unless review lookup is needed. <br>


## Reference(s): <br>
- [TGO Yemek API Quick Reference](references/api-quick-ref.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/rersozlu/skills/food402) <br>
- [Publisher Profile](https://clawhub.ai/user/rersozlu) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with bash commands and JSON API payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, openssl, TGO_EMAIL, and TGO_PASSWORD; GOOGLE_PLACES_API_KEY is optional for review lookup.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
