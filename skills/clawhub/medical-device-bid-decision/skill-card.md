## Description:

This skill helps agents evaluate whether to bid on medical-device and hospital procurement opportunities by analyzing procurement history, likely competitors, pricing benchmarks, and bid risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External business and procurement teams use this skill to decide whether to pursue a specific hospital or medical-device tender, estimate a defensible bid range, identify likely competitors, and surface bid risks from public tender data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic registration can send a hardware-derived device identifier to the vendor.

Mitigation: Configure ZLBX_API_KEY before use to skip automatic registration and MAC-hash collection.

Risk: The skill stores credentials locally when automatic registration is used.

Mitigation: Protect local credential files and prefer an explicitly managed environment variable for shared or managed environments.

Risk: Generated HTML reports and signed sk links may expose sensitive tender analysis or access-bearing URLs if broadly shared.

Mitigation: Treat generated reports and signed links as sensitive, share them only with intended recipients, and review report contents before distribution.

Risk: The local report renderer has URL-sanitization weaknesses according to the security guidance.

Mitigation: Use API-returned links as documented, avoid manually inserting untrusted links into report JSON, and review generated HTML before opening or sharing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/medical-device-bid-decision)
- [API Quick Reference](references/api-quick.md)
- [Automatic Registration Workflow](references/auto-register.md)
- [Decision Analysis Workflow](references/workflow.md)
- [Report Template](references/report-template.md)
- [ZhiLiaoBiaoXun API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown decision report plus optional self-contained HTML report file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include API-sourced citations, data gaps, estimated credit usage, and absolute local paths for generated HTML reports.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
