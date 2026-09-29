## Description:

Looks up fuel prices across Chinese provinces and advertises historical prices and a nationwide overview.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tangjian18](https://clawhub.ai/user/tangjian18)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents looking up provincial gasoline and diesel prices in China can use this skill to request current prices and, once verified, historical or nationwide comparisons.

### Deployment Geography for Use:

Global (price coverage: China)

## Known Risks and Mitigations:

Risk: API responses may be executed as code by the supplied scripts.

Mitigation: Do not install or run this version until the scripts treat API responses only as data, using static parsing code and stdin or secure temporary files.

Risk: Advertised historical and nationwide views may be misleading or broken.

Mitigation: Verify those features against reliable price sources before relying on their results.

Risk: Adding the skill directory to PATH changes future shell sessions.

Mitigation: Avoid the optional PATH change unless its persistent effect is understood.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/tangjian18/skills/oil-price-query)
- [360 Maps fuel-price data source](https://map.360.cn/app/qcms?req=oil_price)
- [360 Maps province-code data](https://map.360.cn/cms/map/data/region.json)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Plain text and Markdown tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices are presented in CNY per liter; upstream data may be delayed.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
