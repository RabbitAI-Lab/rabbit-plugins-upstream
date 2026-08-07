## Description: <br>
Agent Research guides an agent through A-share investment research using multi-agent debate, limit-up and limit-down rule handling, financial data inputs, and structured research outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask an agent for A-share market analysis, portfolio research, risk-control notes, and structured investment-research reports. Outputs should be treated as informational and reviewed by a human before any investment or trading action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests command execution and may rely on financial data/API-key access for A-share research. <br>
Mitigation: Install only after confirming command execution and financial-data access are appropriate; constrain commands, endpoints, data sources, and credentials in the runtime environment. <br>
Risk: The security evidence flags mixed unrelated SEO triggers and unsupported safety claims. <br>
Mitigation: Review generated instructions and outputs before use, and do not rely on the skill's self-described safety claims without independent validation. <br>
Risk: Financial research output could be mistaken for investment or trading advice. <br>
Mitigation: Treat outputs as informational research support and require human review before any investment or trading action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agent-research) <br>
- [Declared homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with structured JSON examples and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Financial research outputs are informational and should be human-reviewed before investment or trading decisions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
