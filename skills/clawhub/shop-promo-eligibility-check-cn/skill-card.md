## Description:

根据用户提供的已确认优惠规则与购物清单，逐项核对适用条件并给出可追溯的金额计算和应付草稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT-0

## Use Case:

面向电商客服与运营人员，用于复核具体购物订单能否使用已确认的优惠，并查看逐项条件状态、计算依据及应付金额草稿。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A payable draft may misstate the customer price if discount-combination permission or another merchant rule has not been confirmed.

Mitigation: Confirm the applicable rules with the merchant and review the calculated draft before quoting a customer.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xxjrq/skills/shop-promo-eligibility-check-cn)
- [Project repository](https://github.com/xxjrq/shop-promo-eligibility-check-cn)
- [Saleor discount domain reference](https://github.com/saleor/saleor)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Calculation guidance]

**Output Format:** [Structured condition statuses, calculation steps, and a payable draft]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports up to 10 promotions and 20 cart lines. Missing or unconfirmed terms remain pending; it does not fetch live prices, claim coupons, place orders, or identify the lowest price.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
