## Description: <br>
Xinjiang regional tax preference assistant for evaluating preferential enterprise income tax regimes, eligibility thresholds, local-share exemptions, branch taxation, park selection, bonded-zone operating patterns, and compliance self-checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax teams, and business operators use this skill to assess Xinjiang-focused enterprise income tax preference options, evidence requirements, risk indicators, and implementation checklists. It supports planning and self-check workflows but does not replace professional tax, audit, or legal advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and scenarios may be sent to the mcp.aitaxs.top cloud service. <br>
Mitigation: Avoid confidential client, financial, or regulated data unless the endpoint and data handling have been reviewed by the user's organization. <br>
Risk: The skill can create local credential or configuration files and store raw query logs under the user's home directory. <br>
Mitigation: Review local persistence behavior before installation and inspect generated configuration and log paths after setup. <br>
Risk: Automatic MCP client setup can modify client configuration when explicitly enabled. <br>
Mitigation: Do not enable TAX_ENABLE_AUTOSETUP or run init_agent.py directly unless the user intentionally wants client configuration changes. <br>
Risk: The security verdict is suspicious because remote services, local persistence, and setup behavior are broader than the focused tax-description makes clear. <br>
Mitigation: Treat the skill as requiring organizational review before use with sensitive tax or business data. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/zxj2devs/skills/tax-xinjiang-preferential) <br>
- [Xinjiang preferential tax compliance self-check](https://mcp.aitaxs.top/web/topic_workflow_xinjiang_preferential.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with structured checklists, tax scenario analysis, optional configuration snippets, and links to compliance self-check pages.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route tax questions to a remote MCP service and may provide local setup guidance for supported clients.] <br>

## Skill Version(s): <br>
3.15.8 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
