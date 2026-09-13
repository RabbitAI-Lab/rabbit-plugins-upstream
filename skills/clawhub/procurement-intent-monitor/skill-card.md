## Description:

Helps users find early procurement opportunities by scanning proposed projects, procurement-intent notices, and expiring contracts, then ranking results by value and next action.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External business development, sales, and procurement-monitoring users use this skill to discover pre-tender opportunities by industry, region, and budget, then receive ranked opportunity lists with follow-up actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The vendor may receive procurement search terms and, during automatic trial registration, a stable MAC-derived device hash.

Mitigation: Use a manually configured ZLBX_API_KEY when possible and avoid automatic registration unless the user accepts the privacy tradeoff.

Risk: Credentials, generated reports, signed sk links, and auto-login links may be stored or displayed locally and should be treated as sensitive.

Mitigation: Protect ~/.zlbx/config.json, avoid sharing signed or auto-login links broadly, and remove local reports when they are no longer needed.

Risk: The security verdict is suspicious because the skill stores credentials and reports locally while enabling login-bypass links.

Mitigation: Review the skill before installation and install only when the vendor data handling model is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/procurement-intent-monitor)
- [Workflow guide](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Auto-registration flow](references/auto-register.md)
- [Report template](references/report-template.md)
- [Zhiliao Biaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliao Biaoxun skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown opportunity lists and optional self-contained HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ZLBX_API_KEY or local configuration for authenticated vendor API calls; full scans may consume account credits.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
