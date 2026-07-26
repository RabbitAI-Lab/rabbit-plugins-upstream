## Description: <br>
Notify when aircraft are overhead within a configurable radius using a local ADS-B SBS/BaseStation feed (readsb port 30003). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davestarling](https://clawhub.ai/user/davestarling) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to configure, test, and run a periodic ADS-B overhead watcher that detects nearby aircraft from a local SBS/BaseStation feed and sends WhatsApp notifications through Clawdbot. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The configuration can reveal home coordinates and the WhatsApp notification target. <br>
Mitigation: Keep the config private, restrict file permissions, and review the configured home coordinates and notification target before enabling the watcher. <br>
Risk: Optional photo lookup can send observed aircraft identifiers to Planespotters. <br>
Mitigation: Disable photo lookup when external enrichment is not acceptable. <br>
Risk: A cron or timer setup can continue monitoring and sending messages after it is no longer wanted. <br>
Mitigation: Remove the scheduled job or set enabled=false when ongoing monitoring should stop. <br>


## Reference(s): <br>
- [SBS/BaseStation MSG fields](references/sbs-fields.md) <br>
- [ADS-B Overhead on ClawHub](https://clawhub.ai/davestarling/skills/moltbot-adsb-overhead) <br>
- [davestarling ClawHub profile](https://clawhub.ai/user/davestarling) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, configuration examples, and text or JSONL alert output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can emit human-readable alert text or one JSON object per alert; optional photo lookup may add a photo URL or downloaded media path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
