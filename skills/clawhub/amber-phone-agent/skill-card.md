## Description: <br>
Amber gives an agent real phone capabilities through a Twilio or compatible voice bridge, OpenAI Realtime calling, MCP tools, inbound screening, confirmed outbound calls, call logs, transcripts, optional CRM/contact memory, calendar booking, contacts lookup, and a loopback-only dashboard. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[batthis](https://clawhub.ai/user/batthis) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use Amber to connect an agent to real telephone workflows, including inbound screening, explicitly confirmed outbound calls, call-history review, contact lookup, and calendar-assisted scheduling. The skill is intended for configured deployments where the operator manages telephony, AI-provider credentials, caller notice, access control, and retention practices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Amber handles sensitive phone, contact, calendar, transcript, and optional CRM data. <br>
Mitigation: Operate it as a sensitive communications system: keep logs, transcripts, contact caches, and CRM files private; define retention and deletion practices; and enable CRM enrichment or extended contacts only when needed. <br>
Risk: Telephony, AI-provider, and optional OpenClaw credentials can expose real calling and data access if over-scoped or leaked. <br>
Mitigation: Use dedicated least-privilege Twilio, OpenAI, and OpenClaw credentials, keep secrets out of logs, rotate them when needed, and review dependency and configuration changes before deployment. <br>
Risk: A locally served bridge or dashboard may expose call controls or communications records if made reachable without protection. <br>
Mitigation: Keep the bridge and dashboard loopback-only or place them behind authentication and network controls before using real callers. <br>
Risk: Real calls may involve people who did not configure the system and may be recorded or transcribed. <br>
Mitigation: Configure caller notice and consent appropriate to the deployment, and require explicit confirmation before outbound calls, calendar writes, payments, commitments, or escalation-sensitive actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/batthis/skills/amber-phone-agent) <br>
- [Amber repository](https://github.com/batthis/amber-openclaw-voice-agent) <br>
- [Architecture](references/architecture.md) <br>
- [Release checklist](references/release-checklist.md) <br>
- [Runtime README](runtime/README.md) <br>
- [Hermes package README](packaging/hermes/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown instructions with code blocks and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are operator-facing setup, verification, and usage guidance for connecting Amber runtime and MCP tools to an agent.] <br>

## Skill Version(s): <br>
5.5.45 (source: server release metadata and runtime/package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
