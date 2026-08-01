## Description: <br>
Chinese-language tax compliance assistant for Hainan Free Trade Port substantive-operation checks, preferential tax treatment, talent individual-income-tax relief, customs-closure transition issues, shell-company risk identification, and practical remediation planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External businesses, tax teams, and advisors use this skill to assess whether Hainan Free Trade Port entities and talent arrangements meet substantive-operation and preferential-tax conditions. It supports question answering, risk self-checks, calculation-oriented tax guidance, report drafting, and offline fallback checklists. <br>

### Deployment Geography for Use: <br>
China (Hainan Free Trade Port tax-compliance use cases) <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax questions, risk scenarios, and calculation inputs may be processed by the remote service mcp.aitaxs.top. <br>
Mitigation: Avoid entering confidential identifiers or unreleased business details unless the user trusts that service; use sanitized scenarios for initial analysis. <br>
Risk: The client stores local API and log data under ~/.tax-policy-client, which may remain on shared machines. <br>
Mitigation: Review or clear ~/.tax-policy-client logs and configuration after use on shared or managed devices. <br>
Risk: The security evidence marks the release suspicious because remote processing and local storage are not sufficiently disclosed to users. <br>
Mitigation: Review the security summary and installation prompts before deployment, especially when enabling the full tax-skill matrix or MCP integrations. <br>
Risk: Tax outputs may be incomplete, stale, or unsuitable as final filing, audit, legal, or tax advice. <br>
Mitigation: Validate material conclusions against official policy sources and qualified tax or legal professionals before filing, claiming benefits, or taking remediation steps. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-hainan-ftp) <br>
- [Hainan FTP compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_hainan_ftp.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured text with optional JSON-like tool results, copied plain-text reports, shell commands, and MCP configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP tools for policy questions, risk checks, tax calculations, and knowledge-base metadata; offline scripts provide fallback process guidance and keyword checks.] <br>

## Skill Version(s): <br>
3.15.6 (source: frontmatter and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
