## Description: <br>
BuyWise is a shopping advisor that helps users decide whether to buy, where to buy, and when to buy across major global and Chinese shopping platforms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiajiaoy](https://clawhub.ai/user/jiajiaoy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and shopping assistants use BuyWise to evaluate products before purchase, compare prices across major international and Chinese retailers, check discount authenticity, summarize public reviews, and decide whether to buy now or wait. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product names or links may be sent to external shopping, search, price-history, and review sites during research. <br>
Mitigation: Avoid entering sensitive purchase details and review which external sites the assistant is asked to open before proceeding. <br>
Risk: Prices, availability, discounts, and review summaries can be stale or incomplete. <br>
Mitigation: Confirm retailer prices and terms on the source platform before buying. <br>
Risk: CouponClaw follow-up actions are separate from the BuyWise analysis. <br>
Mitigation: Approve any coupon or cashback lookup deliberately before running a separate skill. <br>


## Reference(s): <br>
- [BuyWise ClawHub Skill Page](https://clawhub.ai/jiajiaoy/skills/buywise) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [BuyWise README](artifact/README.md) <br>
- [BuyWise Skill Definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown shopping analysis guidance with comparison tables, verdicts, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include browser navigation targets for public shopping, price-history, and review sites.] <br>

## Skill Version(s): <br>
1.5.7 (source: package.json, _meta.json, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
