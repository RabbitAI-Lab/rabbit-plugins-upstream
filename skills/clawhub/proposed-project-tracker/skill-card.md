## Description:

This skill helps agents find early business opportunities by scanning proposed projects, procurement intentions, and expiring contracts through Zhiliaobiaoxun.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Business development, sales, and bid teams use this skill to scan for earlier-stage commercial opportunities by industry, product, region, and budget threshold. It ranks proposed projects, procurement intentions, and expiring contracts, then recommends next actions for follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user opportunity search terms to Zhiliaobiaoxun services.

Mitigation: Use the skill only when vendor API processing is acceptable, and avoid sending sensitive internal strategy, customer data, or confidential project details as search terms.

Risk: Automatic registration can derive a MAC-based device hash and persist a vendor API key under the user's home directory.

Mitigation: Prefer a user-provided ZLBX_API_KEY when available, require consent before auto-registration, and review local credential file permissions after first use.

Risk: Generated reports and opportunity links may contain login-bypass or signed access parameters.

Mitigation: Review reports before sharing and avoid forwarding generated HTML reports or signed links beyond the intended recipients.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/proposed-project-tracker)
- [Workflow Guide](references/workflow.md)
- [API Quick Reference](references/api-quick.md)
- [Report Template](references/report-template.md)
- [Auto-Registration Flow](references/auto-register.md)
- [Zhiliaobiaoxun API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun Skill Documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Zhiliaobiaoxun Opportunity Assistant](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown opportunity lists, JSON report data, and generated self-contained HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include signed opportunity links and locally saved HTML reports.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
