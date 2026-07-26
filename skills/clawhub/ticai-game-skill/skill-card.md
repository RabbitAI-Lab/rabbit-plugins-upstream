## Description: <br>
中国体育彩票全玩法号码分析、条件筛选、走势图、历史数据查询与数据参考综合工具，覆盖超级大乐透、排列3、排列5、七星彩、竞彩足球、竞彩篮球、传统足彩全部玩法。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xljcheng](https://clawhub.ai/user/xljcheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to analyze China Sports Lottery data, filter number sets, generate trend reports, validate CSV data, and run supporting command-line tools for statistical reference. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lottery analysis output may be mistaken for betting advice or a prediction. <br>
Mitigation: Keep outputs framed as statistical references only, preserve the no-prediction/no-betting caveat, and require users to make independent decisions. <br>
Risk: User-invoked tools can read CSV files and write generated CSV, HTML, or cache files. <br>
Mitigation: Run tools only against intended local files and review output paths before execution. <br>
Risk: The optional data-fetching tool can contact public lottery data sites. <br>
Mitigation: Use the fetch workflow only where outbound public-data requests are permitted, or rely on user-provided CSV data instead. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xljcheng/skills/ticai-game-skill) <br>
- [500star public lottery data chart](https://datachart.500star.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and terminal text with optional CSV or HTML files from user-invoked scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are statistical references for lottery data analysis and should not be treated as betting advice.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter also lists 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
