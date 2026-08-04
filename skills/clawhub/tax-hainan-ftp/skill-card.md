## Description: <br>
Provides Hainan Free Trade Port tax compliance guidance for substantive operations, preferential tax treatment, talent individual income tax, encouraged-industry qualification, risk self-checks, and remediation planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business users, tax teams, and advisors use this skill to assess Hainan Free Trade Port tax incentive eligibility, substantive-operation requirements, risk indicators, and practical remediation steps. <br>

### Deployment Geography for Use: <br>
China (Hainan Free Trade Port) <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax or business details may be sent to mcp.aitaxs.top and, during fallback, to public search services. <br>
Mitigation: Avoid entering confidential identifiers unless necessary, minimize scenario details, and use offline reference mode for sensitive preliminary review. <br>
Risk: API keys, health state, feedback queue data, cache files, and logs may be stored under ~/.tax-policy-client. <br>
Mitigation: Review or delete local ~/.tax-policy-client files as needed and manage stored credentials according to local security policy. <br>
Risk: Auto-setup behavior can modify local MCP client configuration when explicitly run or when TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Do not run config/init_agent.py or set TAX_ENABLE_AUTOSETUP=1 unless you intend to add or update local MCP configuration. <br>
Risk: Tax outputs are guidance and self-check aids, not binding tax, audit, or legal opinions. <br>
Mitigation: Verify material conclusions against official policy sources and qualified tax or legal professionals before filing or relying on the results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-hainan-ftp) <br>
- [Hainan FTP compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_hainan_ftp.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration, shell commands] <br>
**Output Format:** [Markdown and structured text, with optional generated compliance report text and local command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote MCP tax-policy tools, provide offline fallback guidance, and link to a browser-based self-check workflow.] <br>

## Skill Version(s): <br>
3.15.10 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
