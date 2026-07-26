## Description: <br>
Local-first budget and policy guardrails for agent actions, with optional remote sync to AgentSentinel. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jimmystacks](https://clawhub.ai/user/jimmystacks) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to check proposed commands against local policy and budget limits before execution, then optionally sync logged events to AgentSentinel for centralized visibility. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local event logs can contain command text, paths, and operational context. <br>
Mitigation: Treat .agent-sentinel/openclaw_events.jsonl as sensitive, limit access to it, and review its contents before sharing or syncing. <br>
Risk: Cloud sync uploads locally recorded action events to AgentSentinel when AGENT_SENTINEL_API_KEY is set and sync is run. <br>
Mitigation: Only set AGENT_SENTINEL_API_KEY and run sync when the operator trusts AgentSentinel with those logged events. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/jimmystacks/skills/agent-sentinel) <br>
- [AgentSentinel skill homepage](https://github.com/jimmystacks/agent-sentinel/tree/main/skills/agent-sentinel) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [JSON command responses with Markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local state is stored under .agent-sentinel; optional cloud sync requires AGENT_SENTINEL_API_KEY and an explicit sync command.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release evidence and CHANGELOG.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
