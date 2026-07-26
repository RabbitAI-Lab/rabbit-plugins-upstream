## Description: <br>
Build high-performing OpenClaw agents end-to-end, including persona, operating rules, guardrails, and required workspace files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[IceMasterT](https://clawhub.ai/user/IceMasterT) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and advanced OpenClaw users use this skill to design new agents, generate complete OpenClaw workspace files, and iteratively refine agent behavior, autonomy, guardrails, tone, memory, heartbeat, and skill roster. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated agent workspaces can encode excessive autonomy, especially when broad delegation or autopilot behavior is requested. <br>
Mitigation: Review SOUL.md, AGENTS.md, and HEARTBEAT.md before use and prefer conservative autonomy unless broader delegation is intentional. <br>
Risk: Generated memory files could contain secrets or sensitive personal information if the user provides them during setup. <br>
Mitigation: Do not store secrets in MEMORY.md or daily memory logs; keep credentials and private transcripts outside the workspace. <br>
Risk: Publisher or package identity may need confirmation because artifact metadata does not exactly match the registry context. <br>
Mitigation: Verify the ClawHub publisher handle and package identity before deployment. <br>


## Reference(s): <br>
- [Agent Builder release page](https://clawhub.ai/IceMasterT/agent-builder-1-0-0) <br>
- [OpenClaw workspace](references/openclaw-workspace.md) <br>
- [Templates](references/templates.md) <br>
- [Architecture](references/architecture.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance and generated workspace file content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce OpenClaw workspace file drafts such as IDENTITY.md, SOUL.md, AGENTS.md, USER.md, HEARTBEAT.md, MEMORY.md, and TOOLS.md.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
