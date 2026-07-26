## Description: <br>
Monitors Chinese procurement intent notices, proposed projects, and expiring contracts to help users find early procurement opportunities before formal bidding. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business development, sales, and procurement teams use this skill to scan Chinese public procurement signals, rank opportunities, track progress, and generate shareable opportunity reports. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Procurement search terms are sent to a third-party vendor API. <br>
Mitigation: Review queries before use and avoid sending confidential opportunity names, customer lists, or internal strategy terms. <br>
Risk: API credentials may be stored in ~/.zlbx/config.json. <br>
Mitigation: Prefer a preconfigured environment variable when possible, restrict local file access, and rotate the key if the configuration file is exposed. <br>
Risk: Trial auto-registration may collect a stable hashed MAC-derived device identifier after consent. <br>
Mitigation: Require explicit user consent before registration, or preconfigure ZLBX_API_KEY to bypass auto-registration. <br>
Risk: Generated chat output or HTML reports may include login-bypass links. <br>
Mitigation: Share generated reports only with intended recipients and remove access links when reports need broader distribution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/procurement-intent-monitor) <br>
- [API quick reference](artifact/references/api-quick.md) <br>
- [Workflow guide](artifact/references/workflow.md) <br>
- [Report template](artifact/references/report-template.md) <br>
- [Auto-registration guide](artifact/references/auto-register.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, HTML, guidance] <br>
**Output Format:** [Markdown opportunity lists in chat, with optional self-contained HTML reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-consented auto-registration; may write reports under ~/zlbx-opportunity-radar-files/.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
