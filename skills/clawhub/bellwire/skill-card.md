## Description: <br>
Add, update, test, diagnose, or maintain Bellwire live cards and phone notifications in Node.js, Cloudflare Worker, and shell projects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xwchris](https://clawhub.ai/user/xwchris) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to connect repository events, health, metrics, payments, deployments, jobs, or other project state to Bellwire live cards, inbox entries, and phone notifications. It guides binding, project setup, Event Specs, live Surfaces, webhook adapters, testing, delivery checks, and troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bellwire tokens or sensitive event fields could be exposed in tracked files, logs, telemetry, test snapshots, or notification templates. <br>
Mitigation: Store tokens only in an approved secret store, avoid logging payloads or authorization headers, and mark personal, customer, or credential fields as sensitive. <br>
Risk: Destructive or interruptive operations such as deleting projects or enabling high-priority notifications could affect users unexpectedly. <br>
Mitigation: Require explicit confirmation before deleting projects or requesting high-priority notifications, and verify the exact project and notification intent first. <br>
Risk: Manual tests or server acceptance can be mistaken for production notification delivery. <br>
Mitigation: Use the documented production verification gate and confirm real source operations, Bellwire readback, delivery status, and any claimed device presentation. <br>


## Reference(s): <br>
- [Bellwire ClawHub skill page](https://clawhub.ai/xwchris/skills/bellwire) <br>
- [GitHub repository](https://github.com/xwchris/bellwire.git) <br>
- [Integration adapters](references/adapters.md) <br>
- [Bellwire API](references/api.md) <br>
- [Event Spec](references/event-spec.md) <br>
- [Production verification](references/production-verification.md) <br>
- [Security](references/security.md) <br>
- [Surfaces](references/surfaces.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Webhooks](references/webhooks.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash, TypeScript, YAML, JSON, and HTTP examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Bellwire API calls and configuration changes that depend on user-provided tokens and project identifiers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
