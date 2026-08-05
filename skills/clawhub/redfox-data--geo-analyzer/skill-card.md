## Description: <br>
GEO（生成式引擎优化）品牌分析工具。自动向豆包、Kimi、DeepSeek 三个 AI 搜索引擎提问，分析品牌在 AI 回答中的出现率、情绪、信源引用、竞品对比，生成交互式 HTML 报告。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External brand marketers, product managers, and content operators use this skill to measure brand visibility in AI search answers, compare competitors, inspect cited sources, and generate GEO optimization findings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Brand, category, competitor, and question data is sent to RedFox-backed external AI search services. <br>
Mitigation: Use only non-confidential inputs and review whether the external service is acceptable for the intended business context before running the skill. <br>
Risk: The generated report summary can falsely claim there were no negative results. <br>
Mitigation: Cross-check the detailed sentiment sections and raw results before relying on summary-level claims. <br>
Risk: The skill requires a REDFOX_API_KEY credential. <br>
Mitigation: Verify the key source, scope, expiration, and revocation process; do not hardcode or expose the key in prompts, logs, code, or output files. <br>


## Reference(s): <br>
- [GEO Metrics Reference](references/geo-metrics.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/redfox-data/skills/geo-analyzer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, HTML files, guidance] <br>
**Output Format:** [Natural-language findings with shell commands, JSON analysis artifacts, and an interactive HTML report.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY and sends brand, category, competitor, and question data to RedFox-backed external AI search services.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
