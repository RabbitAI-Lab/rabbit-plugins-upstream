## Description:

查询中国各省和直辖市的当前油价、历史调价记录及全国油价概览。

This skill is ready for commercial/non-commercial use.

## Publisher:

[tangjian18](https://clawhub.ai/user/tangjian18)

### License/Terms of Use:

MIT-0

## Use Case:

Users and agents can look up Chinese provincial gasoline and diesel prices and review reported price changes. Historical and nationwide results require independent checking before reliance.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: A reachable parsing flaw can treat an external API response as executable Python source.

Mitigation: Fix the affected scripts to parse responses strictly as data and review them before installation or execution.

Risk: Historical and nationwide results may not match the requested province or promised coverage.

Mitigation: Check the returned province and coverage, and verify important prices against an authoritative source.

Risk: Installation instructions can make persistent changes to the shell PATH.

Mitigation: Avoid adding the scripts directory to ~/.bashrc unless persistent PATH changes are intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/tangjian18/skills/oil-price-query)
- [360 Maps oil price data](https://map.360.cn/app/qcms?req=oil_price)
- [360 Maps province codes](https://map.360.cn/cms/map/data/region.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Plain-text price listings and tables, with command-line usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices are shown in CNY per liter; availability and accuracy depend on the external data source.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
