## Description: <br>
Filtmall Shopping helps agents search, compare, cart, checkout, pay, and follow up on consumer shopping requests through the bundled Filtalgo CLI while keeping authorization and payment control with the user. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[filtmall](https://clawhub.ai/user/filtmall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and shopping agents use this skill to turn natural-language shopping intent into live product search, comparison, cart, checkout, payment-link, order, logistics, address, refund, and after-sales workflows. The user should confirm SKU, quantity, address, amount, and payment intent before high-impact actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent-executable checkout actions can advance or complete purchases. <br>
Mitigation: Require explicit user confirmation of SKU, quantity, address, amount, and payment intent before checkout or payment actions; do not allow automatic checkout completion. <br>
Risk: The skill can operate with a Filtmall session for account, cart, checkout, order, logistics, address, customer-service, and after-sales actions. <br>
Mitigation: Install only when comfortable granting shopping-session access, avoid exposing session identifiers or tokens, and revoke the session with auth logout when finished. <br>
Risk: Live prices, stock, specifications, and links may change during shopping. <br>
Mitigation: Treat CLI-returned product, price, stock, SKU, order, and URL data as the source of truth and re-check live results before purchase decisions. <br>
Risk: Beauty and personal-care shopping can intersect with active health symptoms. <br>
Mitigation: Do not search for or recommend cosmetics for active allergic reactions, redness, swelling, or similar symptoms; advise professional medical care instead. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/filtmall/skills/filtmall-shopping) <br>
- [Filtmall website](https://www.filtalgo.com/) <br>
- [About Filtmall](https://www.filtalgo.com/about) <br>
- [Official LLM reference](https://www.filtalgo.com/llms.txt) <br>
- [Machine-readable service directory](https://www.filtalgo.com/agents.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured JSON CLI results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 18 or later; account, checkout, order, address, customer-service, and after-sales actions require a valid Filtmall session.] <br>

## Skill Version(s): <br>
1.3.0 (source: evidence release, skill metadata, README) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
