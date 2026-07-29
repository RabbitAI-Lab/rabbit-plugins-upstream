## Description: <br>
This skill helps users assess Hainan Free Trade Port tax incentives, substantial-operation requirements, personal income tax treatment, offshore investment deductions, customs-closure changes, and shell-company compliance risks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business advisers use this skill to evaluate Hainan Free Trade Port tax-compliance scenarios, prepare self-checks, and understand risk indicators before seeking qualified professional review. <br>

### Deployment Geography for Use: <br>
China, with subject-matter focus on the Hainan Free Trade Port. <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, business scenarios, and self-check metrics may be sent to mcp.aitaxs.top, and fallback behavior may query public search engines. <br>
Mitigation: Avoid entering confidential client, payroll, identity, or unpublished business details unless approved, and review remote data-flow expectations before installation. <br>
Risk: Local API keys, configuration, logs, or browser-local authentication state may persist after use. <br>
Mitigation: Clear browser localStorage API keys and remove ~/.tax-policy-client logs and configuration when the skill is no longer needed. <br>
Risk: Optional setup behavior can modify supported MCP client configuration when explicitly enabled. <br>
Mitigation: Review or disable autosetup/config-writing behavior, and keep default dry-run behavior unless configuration changes are approved. <br>
Risk: Tax calculations and compliance conclusions are auxiliary guidance and may not match a regulator's or licensed professional's final assessment. <br>
Mitigation: Treat outputs as self-check support, verify policy timing and facts against official sources, and consult qualified tax or legal professionals for material filings or disputes. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/zxj2devs/skills/tax-hainan-ftp) <br>
- [Hainan FTP compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_hainan_ftp.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown and plain text guidance, with optional configuration snippets and self-check report content.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include risk scores, checklists, policy-source references, and remediation steps for user-provided tax scenarios.] <br>

## Skill Version(s): <br>
3.15.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
