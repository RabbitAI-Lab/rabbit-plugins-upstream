## Description: <br>
OpenCode+OMO orchestration: keep this session as decision maker/integrator; for non-trivial work prefer bounded available agents for search, reading, research, testing, review, and mutually exclusive writes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[its-how](https://clawhub.ai/user/its-how) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers using OpenCode with OMO use this skill to orchestrate non-trivial agent work across native capabilities, OMO agents, subagents, review lanes, and bounded write lanes while preserving primary-session decision making and verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may change how work is split across agents, which can affect cost, latency, write coordination, or review boundaries. <br>
Mitigation: Keep the primary session as decision maker and final integrator, require secondary confirmation for large fan-out, worktree, cross-domain, persistent, or high-cost routes, and use bounded mutually exclusive write sets for delegated writes. <br>
Risk: Delegation or handoff material could expose sensitive session, credential, provider, browser, or account state if local rules are ignored. <br>
Mitigation: Exclude credentials, tokens, cookies, browser sessions, provider state, live account state, and secret-derived material from delegation and handoffs, and keep stricter project and permission rules in force for sensitive repositories. <br>
Risk: An agent could overclaim unavailable OpenCode or OMO capability surfaces. <br>
Mitigation: Detect OMO and specific agent or feature surfaces before use, skip only unavailable surfaces, and transparently fall back to native OpenCode capabilities when OMO is not installed. <br>


## Reference(s): <br>
- [Aha Opencode Omo on ClawHub](https://clawhub.ai/its-how/skills/aha-opencode-omo) <br>
- [aha-orch repository](https://github.com/its-How/aha-orch) <br>
- [Capability Orchestration](references/capability-orchestration.md) <br>
- [OpenCode](https://github.com/sst/opencode) <br>
- [oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured routing criteria] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent-facing orchestration guidance; no runtime state is persisted by the skill.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
