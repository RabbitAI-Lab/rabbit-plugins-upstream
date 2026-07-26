## Description: <br>
Navigate Taobao with public product research, seller verification, review reading, price comparison, SKU risk checks, and cart-ready guidance while keeping login, address, checkout, order submission, and payment under user control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[harrylabsj](https://clawhub.ai/user/harrylabsj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External shoppers use this skill to research Taobao listings, compare public seller and product signals, summarize visible discounts and reviews, and prepare a manual checkout checklist. It is intended for decision support before the user handles any private account, cart, checkout, order, or payment action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent could overstep into private shopping actions such as login, cart changes, coupon application, checkout, order submission, or payment. <br>
Mitigation: Stop before private account or purchase state and provide only cart-ready guidance; the user manually handles login, address, coupons, checkout, order submission, and payment. <br>
Risk: Public Taobao pricing, stock, delivery, seller ratings, and promotion terms can be incomplete or change before purchase. <br>
Mitigation: Treat outputs as decision support, snapshot visible public details, and ask the user to verify final payable amount, stock, delivery, coupon eligibility, return policy, invoice, and warranty before buying. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/harrylabsj/skills/taobao-shopping) <br>
- [Browser workflow](references/browser-workflow.md) <br>
- [Marketplace guide](references/marketplace-guide.md) <br>
- [Output patterns](references/output-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, analysis, guidance] <br>
**Output Format:** [Markdown summaries, comparison tables, and manual pre-checkout checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses public product, seller, pricing, promotion, and review information; private account and purchase steps remain user-controlled.] <br>

## Skill Version(s): <br>
2.1.3 (source: server release evidence, package.json, clawhub.json, README changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
