## Description: <br>
将客户声音(VOC)转化为关键质量特性(CTQ)的分析工具，支持文本分析、需求提取、映射关联、优先级评估和可视化报告生成。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality, product, and customer-experience teams use this skill to analyze customer feedback, extract product or service requirements, map VOC items to CTQ candidates, and prioritize quality improvements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer feedback may include personal, account, or regulated data. <br>
Mitigation: Redact unnecessary sensitive data before analysis and store generated JSON and HTML reports in an appropriate location. <br>
Risk: Generated reports contain customer-derived content that may be inappropriate for broad sharing. <br>
Mitigation: Review generated reports before sharing outside the intended audience. <br>
Risk: Sentiment analysis and CTQ prioritization can be limited for sarcasm, ambiguous language, or domain-specific terminology. <br>
Mitigation: Use human review for important decisions and add a custom user dictionary for domain terms when needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/duding-engicool/skills/skill-voc-ctq-analyzer) <br>
- [Publisher Profile](https://clawhub.ai/user/duding-engicool) <br>
- [Server-Resolved GitHub Provenance](https://github.com/duding-engicool/skill-voc-ctq-analyzer) <br>
- [VOC-CTQ Data Format Specification](references/format_spec.md) <br>
- [VOC Analyzer Script](scripts/voc_analyzer.py) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, json, html, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON analysis artifacts, and HTML visualization reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads local JSON, CSV, or TXT customer feedback and writes local JSON outputs and HTML reports.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
