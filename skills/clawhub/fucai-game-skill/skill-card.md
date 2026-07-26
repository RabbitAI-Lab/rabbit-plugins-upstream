## Description: <br>
中国福利彩票号码筛选与分析技能，支持双色球、福彩3D、七乐彩、快乐8、东方6+1 和 15选5 的开奖结果查询、条件过滤、冷热号统计、走势分析和方案生成。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xljcheng](https://clawhub.ai/user/xljcheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to query China Welfare Lottery results, filter candidate number combinations, analyze recent trends, and format informational lottery reports across supported games. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generic Chinese terms such as filtering, trend, or results may route the agent to this lottery skill when the user meant a different context. <br>
Mitigation: Confirm the lottery game and user intent when wording is ambiguous, and state the selected game before giving results or recommendations. <br>
Risk: Lottery results, trend analysis, and generated recommendations may be incorrect, stale, or mistaken for a financial strategy. <br>
Mitigation: Verify official results independently and present all number recommendations as informational, not as guarantees or investment advice. <br>


## Reference(s): <br>
- [福彩过滤规则参考](artifact/references/filter-rules.md) <br>
- [ClawHub skill page](https://clawhub.ai/xljcheng/skills/fucai-game-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Code, Files, Guidance] <br>
**Output Format:** [Markdown reports, lottery number lists, shell command examples, and generated chart files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use local CSV caches and generated PNG charts; lottery analysis and recommendations are informational only.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
