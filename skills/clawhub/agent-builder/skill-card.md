## Description: <br>
Builds high-performing OpenClaw agents end-to-end by helping design a new agent and generate its required workspace files, or by iterating on an existing agent's behavior, guardrails, autonomy model, heartbeat plan, and skill roster. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[plgonzalezrx8](https://clawhub.ai/user/plgonzalezrx8) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and advanced OpenClaw users use this skill to create or refine an OpenClaw agent workspace with persona, operating rules, memory guidance, heartbeat behavior, guardrails, and acceptance-test scenarios. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated autonomy, memory, or heartbeat settings may be broader than intended. <br>
Mitigation: Review AGENTS.md, SOUL.md, MEMORY.md, and HEARTBEAT.md before using generated files; keep heartbeats empty until intentionally enabled and choose broad autonomy only when desired. <br>
Risk: Workspace memory or generated files may capture sensitive information if users store secrets or session details there. <br>
Mitigation: Avoid storing secrets, credentials, OAuth tokens, API keys, and session transcripts in the agent workspace or memory files. <br>
Risk: An agent built from the generated workspace could take destructive actions or send outbound messages if guardrails are weakened. <br>
Mitigation: Keep explicit ask-before-destructive and ask-before-outbound-message rules, then run short acceptance-test scenarios before deployment. <br>


## Reference(s): <br>
- [OpenClaw agent workspace cheat sheet](references/openclaw-workspace.md) <br>
- [OpenClaw agent file templates](references/templates.md) <br>
- [Agent architecture patterns](references/architecture.md) <br>
- [ClawHub skill page](https://clawhub.ai/plgonzalezrx8/skills/agent-builder) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown workspace files, targeted diffs, checklists, and scenario prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces OpenClaw workspace files such as IDENTITY.md, SOUL.md, AGENTS.md, USER.md, HEARTBEAT.md, optional memory files, and acceptance-test prompts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, created 2026-02-01) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
