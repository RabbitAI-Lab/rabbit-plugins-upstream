## Description: <br>
Provides metallurgy-industry tax compliance guidance, risk self-checks, calculations, policy tracing, examples, and report-oriented remediation support for ferrous, non-ferrous, rare-earth, and precious-metal businesses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax teams, compliance staff, and advisors use this skill to assess Chinese metallurgy tax scenarios, identify risk indicators, trace policy context, and draft practical remediation or self-check reports. It is advisory support only and does not replace licensed tax, audit, or legal review. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, scenarios, and self-check metrics may contain sensitive business information and may be sent to a remote MCP service, public search fallback, or local logs. <br>
Mitigation: Use sanitized inputs for sensitive matters, get approval before remote use in professional environments, and review or clear ~/.tax-policy-client when persisted identifiers, API keys, cache, or logs are not desired. <br>
Risk: Optional automatic setup can modify supported MCP client configuration files when explicitly enabled. <br>
Mitigation: Keep setup in its default dry-run posture unless configuration changes are intended; inspect proposed client config entries and backups before enabling TAX_ENABLE_AUTOSETUP or non-dry-run setup. <br>
Risk: Generated tax calculations, risk scores, and remediation guidance may be incomplete, outdated, or unsuitable for a specific taxpayer's facts. <br>
Mitigation: Treat outputs as decision support, verify policy currency and factual assumptions, and consult qualified tax, audit, or legal professionals before filing, dispute, or high-impact compliance actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-steel) <br>
- [Metallurgy compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_steel.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Analysis, Markdown, JSON, Configuration instructions] <br>
**Output Format:** [Natural-language answers, Markdown reports, structured JSON tool results, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP services, local fallback logic, cached results, local logs, and a browser-based self-check workflow.] <br>

## Skill Version(s): <br>
3.15.6 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
