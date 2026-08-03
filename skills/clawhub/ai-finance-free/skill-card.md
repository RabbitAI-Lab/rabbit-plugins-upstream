## Description: <br>
Ai Finance Free helps an agent respond to natural-language finance analysis requests with structured market queries, analysis reports, exports, and monitoring workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and enterprise teams use this skill to ask an agent for financial analysis, market data interpretation, portfolio or risk review, and report/export workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests exec-enabled finance workflows and API key configuration. <br>
Mitigation: Review the skill before installation, grant only the minimum execution access needed, and use non-sensitive finance data unless the deployment owner accepts the exposure. <br>
Risk: The skill can propose exports, scheduled tasks, monitoring alerts, and portfolio-related actions without clearly documented limits. <br>
Mitigation: Require explicit user confirmation before exports, recurring jobs, alerts, or portfolio-affecting actions, and review where generated files or history are stored. <br>
Risk: Generated finance analysis may be treated as investment guidance even when based on incomplete or delayed data. <br>
Mitigation: Require human review of financial conclusions, data sources, and assumptions before making investment, trading, or compliance decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-finance-free) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON, with occasional shell command snippets for environment setup.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require FINANCE_API_KEY and user-provided or public financial data sources.] <br>

## Skill Version(s): <br>
1.0.0 (source: target metadata, release evidence, frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
