## Description:

Helps users find early construction and infrastructure opportunities by scanning proposed projects, purchase intentions, and expiring service contracts, then ranking leads with suggested next actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External business development, sales, and bid teams use this skill to identify China construction-market leads before formal tender release. It produces a ranked opportunity list and shareable report from proposed-project approvals, purchase-intention notices, and expiring-contract windows.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill can consume paid or trial Zhiliaobiaoxun API quota during scans.

Mitigation: Tell users the expected credit cost before scanning and pause for approval before exceeding the documented call budget.

Risk: The skill may create or use a local API key file and can perform device-derived auto-registration when no key is configured.

Mitigation: Prefer a user-supplied ZLBX_API_KEY for managed environments, require consent before registration, and avoid exposing API keys in conversation or reports.

Risk: Generated reports and chat output can contain login-bypass sk links returned by the vendor service.

Mitigation: Treat generated reports and links as sensitive and share them only with trusted recipients.

Risk: The skill writes persistent HTML reports to the local filesystem.

Mitigation: Review generated reports before distribution and remove local report files when they are no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/construction-project-opportunity-radar)
- [Publisher Profile](https://clawhub.ai/user/dragonzu)
- [API Quick Reference](references/api-quick.md)
- [Auto Registration Flow](references/auto-register.md)
- [Report Template](references/report-template.md)
- [Workflow Guide](references/workflow.md)
- [Zhiliaobiaoxun API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun AI Platform](https://ai.zhiliaobiaoxun.com/?ch=s102)

## Skill Output:

**Output Type(s):** [text, markdown, HTML files, configuration, guidance]

**Output Format:** [Markdown lead lists in chat plus optional self-contained HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include ranked opportunities, source links, data notes, disclaimers, and suggested next actions.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
