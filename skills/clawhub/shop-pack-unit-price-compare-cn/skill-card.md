## Description:

输入已确认的2至10种同类商品包装价格、净含量或数量、单位、币种、价格日期及运费口径，交付统一计量单位的单价表、透明算式、可比性判断和按需求量计算的购买包数。适用于采购前核对包装规格；净含量、折算因子、价格口径或币种缺失即说明缺口并标记不可比，不用密度臆测换算。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External shoppers and buyers can compare 2–10 offers for the same product using confirmed package quantities, prices, currencies, dates, and shipping terms. The skill shows the calculations and, when requested, the number of packs needed for a target quantity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incomplete or inconsistent quantities, conversion factors, currencies, price dates, or shipping terms can make a unit-price comparison misleading.

Mitigation: Use confirmed values, keep price dates and shipping terms visible, check the calculations before purchasing, and mark offers incomparable when their basis cannot be aligned.

Risk: The documented install command does not fix the installer version or skill revision, which can make repeat installations retrieve changed content.

Mitigation: When repeatability matters, review the installer and use a fixed, reviewed skill revision.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/xxjrq/skills/shop-pack-unit-price-compare-cn)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown with comparison tables and transparent calculation formulas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A single response with comparability reasons and optional pack-count calculations, based on user-confirmed inputs.]

## Skill Version(s):

1.0.0 (source: manifest.yaml, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
