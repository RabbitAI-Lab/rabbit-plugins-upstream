## Description: <br>
Builds and iterates OpenClaw agent workspaces with persona, operating rules, guardrails, heartbeat behavior, memory structure, and acceptance-test prompts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fuzzyb33s](https://clawhub.ai/user/fuzzyb33s) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and advanced OpenClaw users use this skill to design a new agent workspace or refine an existing agent's behavior, safety boundaries, autonomy level, memory plan, heartbeat plan, and skill roster. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated MEMORY.md, daily memory logs, or workspace notes may accidentally include credentials, private transcripts, or other sensitive information. <br>
Mitigation: Review generated workspace files before use and keep credentials, OAuth tokens, API keys, and private session transcripts outside the workspace. <br>
Risk: Broad autonomy settings or heartbeat instructions can cause unwanted agent actions if accepted without review. <br>
Mitigation: Confirm autonomy level, outbound-message rules, destructive-action rules, and HEARTBEAT.md content before enabling the generated agent. <br>


## Reference(s): <br>
- [OpenClaw agent workspace](references/openclaw-workspace.md) <br>
- [OpenClaw agent file templates](references/templates.md) <br>
- [Agent Architecture Patterns](references/architecture.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown workspace files, tailored instructions, concise checklists, and scenario prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include SOUL.md, IDENTITY.md, AGENTS.md, USER.md, HEARTBEAT.md, optional MEMORY.md, optional memory/YYYY-MM-DD.md, and optional TOOLS.md content.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
