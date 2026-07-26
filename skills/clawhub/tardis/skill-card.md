## Description: <br>
Track elapsed time from a set epoch with tamper-evident locking for uptime, service hours, time since events, sobriety counters, project duration, equipment runtime, and related milestones. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rm289](https://clawhub.ai/user/rm289) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to create, lock, check, verify, list, and export tamper-evident elapsed-time meters for personal, project, equipment, or service-hour tracking. It can also configure milestone notifications and optional SendGrid webhook processing when networked notification features are needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Networked notification and webhook features may send meter or email-event data to SendGrid, Discord, or OpenClaw destinations. <br>
Mitigation: Install these features only when needed, configure destinations explicitly, and review what data is sent before enabling them. <br>
Risk: Public webhook tunneling and background service behavior can expose a local webhook endpoint or restart services unexpectedly. <br>
Mitigation: For local-only use, avoid cloudflared, ngrok, and check-webhook-services.sh; if webhooks are required, supervise the tunnel and enable SendGrid signature verification. <br>
Risk: Broad .env loading can make more secrets available to the scripts than the feature needs. <br>
Mitigation: Use a dedicated least-privilege configuration for notification credentials and restrict access to configuration files. <br>
Risk: Opt-in ACTION milestone triggers can become agent instructions if supporting files are writable by untrusted parties. <br>
Mitigation: Keep ACTION handling disabled unless required and restrict who can edit meters.json and HEARTBEAT.md. <br>


## Reference(s): <br>
- [TARDIS on ClawHub](https://clawhub.ai/rm289/skills/tardis) <br>
- [README](README.md) <br>
- [Technical Whitepaper](WHITEPAPER.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-producing CLI operations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled CLI can emit status text, paper-code verification output, milestone JSON, witness logs, and JSON exports.] <br>

## Skill Version(s): <br>
1.2.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
