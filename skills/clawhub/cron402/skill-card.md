## Description:

Operate existing cron402 or agentcron.site paid webhook jobs, or create new cron402 jobs only after the user explicitly selects cron402, agentcron, or the cron402 MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[userdefault13](https://clawhub.ai/user/userdefault13)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to safely create, fund, inspect, pause, resume, and delete paid cron402 webhook schedules. It is for recurring remote URL calls where the user has explicitly chosen cron402 and confirmed any paid action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid create_cron and topup_cron calls spend USDC from the configured wallet.

Mitigation: Use a dedicated low-balance wallet, check funding first, preview the schedule, get explicit confirmation, and call each paid tool at most once per request.

Risk: Remote webhook jobs can continue running after the agent session ends and may include target request details supplied by the user.

Mitigation: Avoid broad or long-lived credentials in URLs, headers, bodies, or notification URLs; disclose what will be sent, require confirmation for sensitive fields, and rotate target credentials if they may have been disclosed.

## Reference(s):

- [cron402 Skill Page](https://clawhub.ai/userdefault13/skills/cron402)
- [cron402 OpenAPI](https://cron402-api.user-defaults.workers.dev/v1/openapi.json)
- [abracadabra Companion Skill](https://clawhub.ai/userdefault13/skills/abracadabra)
- [Abracadabra Cartridge Documentation](https://github.com/userdefault13/abracadabra/blob/main/docs/CARTRIDGE.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes confirmation gates for paid actions, wallet handling, schedule previews, and credential redaction.]

## Skill Version(s):

1.1.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
