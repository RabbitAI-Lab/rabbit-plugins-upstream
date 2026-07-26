## Description: <br>
Provides Hainan Free Trade Port tax-compliance guidance for substantive operations, tax incentives, talent individual income tax relief, encouraged-industry qualification, offshore investment, customs-closure transition, and shell-company risk self-checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, finance, compliance, and operations teams use this skill to assess Hainan Free Trade Port incentive eligibility, substantive-operation requirements, risk indicators, and remediation steps. It is advisory support only and does not replace licensed tax, audit, or legal review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts a remote tax-policy service and stores a local API key and client ID. <br>
Mitigation: Review the service operator and privacy terms before use, avoid entering sensitive company identifiers, and rotate or remove local credentials when they are no longer needed. <br>
Risk: The skill may log questions locally and can fall back to public search engines. <br>
Mitigation: Use redacted or synthetic facts for sensitive tax scenarios, review local log storage, and verify important tax positions against official sources or qualified professionals. <br>
Risk: The skill includes tooling that can install or replace additional tax skills. <br>
Mitigation: Trigger matrix installation only when broader tax-skill expansion is intended, review the target install directory, and scan newly installed skills before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-hainan-ftp) <br>
- [Hainan FTP compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_hainan_ftp.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown guidance, checklists, risk summaries, web workflow links, and optional local configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote tax-policy MCP service, use a local offline fallback, and guide installation of related tax skills when requested.] <br>

## Skill Version(s): <br>
3.14.38 (source: frontmatter, ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
