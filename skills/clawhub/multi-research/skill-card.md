## Description: <br>
Provides multi-perspective A-share investment research across fundamental, technical, news, and risk dimensions, including composite scoring and investment-oriented analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and financial research workflows use this skill to organize A-share market information, compare fundamental, technical, news, and risk signals, and produce informational research outputs for further review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad command execution in the agent environment. <br>
Mitigation: Install and run only in an environment where command execution is acceptable, and review proposed commands before allowing them to run. <br>
Risk: The skill may require market-data API keys. <br>
Mitigation: Configure only the minimum required API credentials, avoid exposing secrets in prompts or logs, and rotate keys if accidental disclosure is suspected. <br>
Risk: The skill gives investment-oriented recommendations and scores. <br>
Mitigation: Treat outputs as informational research, not personalized financial advice, and independently verify all trading or investment decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/multi-research) <br>
- [Skill Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or structured text with optional JSON examples, code snippets, shell commands, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are informational research aids and should be independently verified before trading or investment decisions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
