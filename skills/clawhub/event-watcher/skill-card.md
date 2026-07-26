## Description: <br>
Event watcher skill for OpenClaw. Use when you need to subscribe to event sources (Redis Streams + webhook JSONL) and wake an agent only when matching events arrive. Covers filtering, dedupe, retry, and session routing via sessions_send/agent_gate. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[solitaire2015](https://clawhub.ai/user/solitaire2015) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to run an OpenClaw event watcher that monitors Redis Streams or webhook JSONL files, filters and deduplicates matching events, and wakes the right session only when delivery criteria are met. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The watcher can automatically wake or message OpenClaw sessions from Redis or webhook events. <br>
Mitigation: Use narrow event filters, explicit reply targets, and least-privilege channel allowlists before running the watcher as a background process. <br>
Risk: Event payloads are local, untrusted inputs that could contain instructions meant for the agent. <br>
Mitigation: Keep the default source safety preamble enabled unless the event source is fully trusted. <br>
Risk: Local session metadata, event logs, and dead-letter files may contain sensitive operational context. <br>
Mitigation: Disable session-store lookup when not needed, restrict access to local files, and rotate or protect logs and dead-letter files. <br>
Risk: Runtime dependencies are declared without pinned versions. <br>
Mitigation: Pin redis and pyyaml versions before production deployment. <br>


## Reference(s): <br>
- [CONFIG.md](references/CONFIG.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/solitaire2015/skills/event-watcher) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, Shell commands, Code] <br>
**Output Format:** [Markdown guidance with YAML configuration examples and shell command usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces watcher setup guidance for Redis Stream and webhook JSONL event sources.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
