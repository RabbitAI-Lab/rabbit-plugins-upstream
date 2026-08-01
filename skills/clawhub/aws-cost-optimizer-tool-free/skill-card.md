## Description: <br>
面向个人开发者与初创团队的 AWS 成本分析技能，支持月度支出概览、按服务和区域分解成本、识别闲置资源并生成基础优化建议。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, startup teams, and DevOps practitioners use this skill to review AWS spend, break down costs by service or region, identify idle resources, and prepare basic savings recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan flags broad activation wording and AWS credential use for review before installation. <br>
Mitigation: Install only for AWS billing and cost analysis, and use a dedicated least-privilege read-only IAM identity. <br>
Risk: Generated commands or recommendations could imply AWS resource changes despite the skill's free-version limitation against automatic optimization. <br>
Mitigation: Review all generated commands before execution and do not allow the skill to make resource changes automatically. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/aws-cost-optimizer-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference AWS Cost Explorer data and generated cost reports; users should review commands before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
