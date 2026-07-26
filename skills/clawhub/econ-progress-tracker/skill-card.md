## Description: <br>
中国经济进展跟踪分析框架，基于S总监的经济诊断模型，采集最新财经新闻后评估社会经济进展是否符合预期路径。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[skfrom](https://clawhub.ai/user/skfrom) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and analysts use this skill to gather current Chinese macroeconomic data and financial news, then apply a structured framework to assess whether economic progress aligns with expected policy, industry, and risk paths. The skill can compare against prior local snapshots when available. <br>

### Deployment Geography for Use: <br>
Global, with analysis centered on China. <br>

## Known Risks and Mitigations: <br>
Risk: The workflow browses external financial, news, and statistics sites, which can disclose research topics to those services. <br>
Mitigation: Use approved public sources for sensitive work and avoid running private or confidential research topics through external browsing. <br>
Risk: The workflow stores dated analysis snapshots locally, creating a history of economic research and conclusions. <br>
Mitigation: Use the snapshot feature only where that local history is acceptable, and remove or redact snapshots that contain sensitive context. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/skfrom/skills/econ-progress-tracker) <br>
- [Complete analysis framework](references/framework.md) <br>
- [National Bureau of Statistics of China](http://www.stats.gov.cn) <br>
- [People's Bank of China](http://www.pbc.gov.cn) <br>
- [Ministry of Finance of China](http://www.mof.gov.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, files] <br>
**Output Format:** [Markdown economic tracking report with dated local snapshot output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses current external financial, news, and statistics sources; may persist dated snapshots under memory/econ-tracker/ for later comparison.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
