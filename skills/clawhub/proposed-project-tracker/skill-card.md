## Description:

Tracks proposed projects, procurement intentions, and expiring public-sector contracts to help users find early business opportunities before formal tenders are published.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External business-development and sales users use this skill to scan Chinese proposed-project, procurement-intention, and contract-renewal data for prioritized opportunity lists. It is intended for opportunity discovery, follow-up planning, and recurring monitoring of early-stage commercial signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may persist account credentials in ~/.zlbx/config.json.

Mitigation: Prefer a preconfigured ZLBX_API_KEY where possible, restrict access to the local config file, and review credential storage before installation.

Risk: Generated chat output or HTML reports may contain signed sk or auto-login links.

Mitigation: Treat generated report files and links as sensitive access material and avoid broad sharing.

Risk: The skill sends search keywords, regions, and related query parameters to the Zhiliaobiaoxun API.

Mitigation: Review intended query content before use and avoid submitting confidential business plans or sensitive local files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/proposed-project-tracker)
- [API Quick Reference](references/api-quick.md)
- [Workflow Guide](references/workflow.md)
- [Report Template](references/report-template.md)
- [Auto Registration Flow](references/auto-register.md)
- [Zhiliaobiaoxun Opportunity Platform](https://agent.zhiliaobiaoxun.com)
- [Zhiliaobiaoxun AI Open Platform](https://ai.zhiliaobiaoxun.com/?ch=s98)

## Skill Output:

**Output Type(s):** [text, markdown, html, guidance]

**Output Format:** [Markdown opportunity list in chat, with an optional self-contained HTML report file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based account setup; report links may include signed access parameters returned by the API.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
