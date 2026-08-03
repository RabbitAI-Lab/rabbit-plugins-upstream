## Description: <br>
Provides Hainan Free Trade Port tax-compliance guidance for encouraged-industry enterprises, high-end talent individual income tax benefits, substance-operation checks, policy tracing, risk self-checks, and practical remediation workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business users, tax professionals, and developers use this skill to assess Hainan Free Trade Port tax incentive eligibility, substance-operation readiness, and compliance risks before preparing filings, reports, or remediation plans. It is advisory and should be reviewed against official tax authority guidance and professional advice before operational use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax scenarios and self-check details may be sent to cloud MCP services or public-search fallback services. <br>
Mitigation: Use anonymized or non-sensitive scenarios unless the user has approved disclosure to those services. <br>
Risk: The skill can store API credentials and local logs. <br>
Mitigation: Review credential and log locations before use, avoid regulated data in prompts, and remove local keys or logs when uninstalling. <br>
Risk: Optional automatic setup can change local MCP client configuration. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP disabled until the exact configuration changes have been reviewed. <br>
Risk: Tax-compliance guidance can be incomplete, stale, or unsuitable for a specific filing position. <br>
Mitigation: Confirm material decisions with official tax authority sources or qualified tax/legal professionals before filing or relying on the output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-hainan-ftp) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Hainan FTP compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_hainan_ftp.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with optional code snippets, shell commands, configuration entries, and generated self-check or report text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use cloud MCP services for current policy answers and local offline workflows for fallback guidance.] <br>

## Skill Version(s): <br>
3.15.8 (source: evidence.release.version and artifact/SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
