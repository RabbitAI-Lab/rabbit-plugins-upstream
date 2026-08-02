## Description: <br>
Provides offshore trust and cross-border family wealth personal income tax guidance, structured compliance self-checks, risk scans, and practical workflow support for China tax scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax teams, and compliance practitioners use this skill to ask offshore trust and cross-border family wealth tax questions, run structured self-checks, and produce risk-oriented compliance guidance. It supports informational workflows and does not replace qualified tax, legal, filing, or authority determinations. <br>

### Deployment Geography for Use: <br>
Global, for China individual income tax scenarios. <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends tax questions, scenarios, and self-check metrics to mcp.aitaxs.top and may use local or browser storage for API credentials and logs. <br>
Mitigation: Use it only if the provider and retention policy are acceptable; avoid entering identifying or highly sensitive wealth, trust, residency, or account details. <br>
Risk: Write-enabled auto-setup can add this MCP service to local agent client configuration when explicitly enabled. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP unset unless installation is intended, and review local client configuration before use. <br>
Risk: Offshore trust tax guidance is time-sensitive and may not resolve disputed filing, structuring, or authority acceptance questions. <br>
Mitigation: Verify current official policy and consult qualified tax or legal professionals before filing, structuring, or relying on outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-offshore-trust) <br>
- [Offshore trust interactive self-check](https://mcp.aitaxs.top/web/topic_workflow_offshore_trust.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [State Taxation Administration official site](https://www.chinatax.gov.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or text guidance with optional JSON tool results, shell commands, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote MCP tax service, provide offline keyword/process guidance when unavailable, and generate copyable compliance report text.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
