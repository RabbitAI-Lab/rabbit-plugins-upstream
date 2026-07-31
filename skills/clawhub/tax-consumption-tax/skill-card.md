## Description: <br>
Provides battery consumption tax guidance for tiered rates, exemption eligibility, CMA report prerequisites, entrusted-processing and import deductions, self-use reporting, compliance self-checks, and risk scans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, finance, compliance, and advisory users can ask battery consumption tax questions, run structured compliance self-checks, scan common risk conditions, and produce practical remediation guidance for China battery consumption tax scenarios. <br>

### Deployment Geography for Use: <br>
Global, with content focused on China battery consumption tax compliance. <br>

## Known Risks and Mitigations: <br>
Risk: Remote tax-policy service access can expose submitted business or tax facts outside the local environment. <br>
Mitigation: Review the remote data flow before installation and avoid entering confidential identifiers or sensitive business details unless the organization has approved that use. <br>
Risk: The package stores local credential, cache, and log files for service access. <br>
Mitigation: Use an account and machine profile appropriate for tax data, restrict local file permissions, and clear stored configuration, cache, and logs according to the organization's retention policy. <br>
Risk: MCP client setup behavior can write or merge client configuration when explicitly enabled. <br>
Mitigation: Keep automatic setup disabled until the proposed MCP configuration is reviewed, then enable it only in environments where the configuration change and backup behavior are acceptable. <br>
Risk: Security evidence classifies the release as suspicious because broad tax-service access is under-disclosed. <br>
Mitigation: Install only after reviewing the advertised tool surface, expected endpoints, and the security summary for fit with the deployment environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-consumption-tax) <br>
- [Interactive battery consumption tax workflow](https://mcp.aitaxs.top/web/topic_workflow_consumption_tax.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands, configuration] <br>
**Output Format:** [Markdown text with structured checklists, risk summaries, remediation guidance, and occasional shell or MCP configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote tax-policy MCP service and may fall back to local offline reference guidance when the service is unavailable.] <br>

## Skill Version(s): <br>
3.15.4 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
