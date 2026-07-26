## Description: <br>
该技能根据寄件地、收件地、重量或体积，使用内置快递价格数据为用户计算并对比多家国内快递渠道的预估费用。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[angerfl](https://clawhub.ai/user/angerfl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
个人寄件用户、电商卖家和批量寄件场景可用该技能输入国内寄收地址及包裹重量或体积，获取快递渠道价格对比、首重续重估算和较低价渠道提示。 <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs a bundled local Python calculator against bundled courier price data. <br>
Mitigation: Install only after reviewing the bundled script and data files, and run it in an environment where local script execution is acceptable. <br>
Risk: Displayed courier prices are estimates from the named provider and may differ from final shipping costs. <br>
Mitigation: Verify the final shipping price with the courier or provider platform before purchasing shipping. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/angerfl/skills/kuaidichaxun) <br>
- [README.md](README.md) <br>
- [Example queries](examples/example_queries.md) <br>
- [Address mapping data](references/address_mapping.json) <br>
- [Courier channel price data](references/all_channels_prices.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown-style conversational text with price tables, fee statistics, route notes, and optional local Python command usage.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are based on bundled courier price data and should be treated as estimates rather than final purchase prices.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
