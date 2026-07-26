## Description: <br>
Generate content for TRMNL e-ink display devices using the TRMNL CSS framework and send via the trmnl CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[peetzweg](https://clawhub.ai/user/peetzweg) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and TRMNL users use this skill to create concise e-ink display layouts, dashboards, notifications, and messages, then validate and send them through the TRMNL CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: TRMNL custom plugin webhook URLs are sensitive and could expose display update access if shared. <br>
Mitigation: Keep webhook URLs out of shared transcripts and configuration examples, and review plugin configuration before sending content. <br>
Risk: Installing trmnl-cli with @latest can pick up unreviewed package changes. <br>
Mitigation: Pin or review the npm CLI package version before installing in controlled or production environments. <br>
Risk: Generated content may include private, account-related, or unsuitable information on a shared physical display. <br>
Mitigation: Preview and validate content before sending, especially when it contains personal, operational, or customer data. <br>
Risk: Payload size and rate limits can cause failed display updates. <br>
Mitigation: Use trmnl validate and the configured account tier before sending larger layouts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/peetzweg/skills/trmnl) <br>
- [TRMNL framework overview](artifact/references/framework-overview.md) <br>
- [TRMNL layout systems](artifact/references/layout-systems.md) <br>
- [TRMNL components reference](artifact/references/components.md) <br>
- [TRMNL CSS utilities](artifact/references/css-utilities.md) <br>
- [TRMNL plugin patterns](artifact/references/patterns.md) <br>
- [TRMNL webhook API reference](artifact/references/webhook-api.md) <br>
- [TRMNL anti-patterns](artifact/assets/anti-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTML snippets and bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces TRMNL framework HTML and CLI validation or send commands for e-ink display updates.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
