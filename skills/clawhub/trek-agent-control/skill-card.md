## Description: <br>
配套 Trek 微信旅行小程序的自动化 Skill。通过认证的远程 MCP，让 Codex、Claude、OpenClaw、Hermes、WorkBuddy 等 Agent 研究国内外目的地、读取或修改行程，并把日程、地点、预订、住宿、费用、清单、待办、附件和协作提案安全同步回小程序。Use when an agent needs to plan domestic or overseas travel, inspect existing Trek data, synchronize structured itinerary fields, upload tickets, or run safe diagnostics with a user-provided Trek Agent Key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[super21-bat](https://clawhub.ai/user/super21-bat) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to connect an assistant to Trek travel data, research trips, update itineraries, synchronize places, reservations, lodging, costs, packing, todos, files, and collaboration proposals, then verify the resulting mini program state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Trek Agent Key grants broad access to the user's Trek travel data. <br>
Mitigation: Use one key per agent, store it in a runtime secret manager when possible, avoid copying it into shared files or logs, and revoke it immediately if exposed or no longer needed. <br>
Risk: Remote MCP writes can alter itinerary, reservation, lodging, budget, task, file, and collaboration data. <br>
Mitigation: Preview high-impact changes, write in small batches, reuse existing entities, and read back the live trip state before reporting synchronization complete. <br>
Risk: Travel plans may contain uncertain facts such as bookings, prices, hours, addresses, or opening status. <br>
Mitigation: Use primary or official sources for current facts, preserve uncertainty as todos or notes, and avoid marking bookings confirmed without order evidence. <br>


## Reference(s): <br>
- [Trek Agent Control on ClawHub](https://clawhub.ai/super21-bat/skills/trek-agent-control) <br>
- [Runtime configuration](references/configuration.md) <br>
- [Dynamic tool and field guide](references/field-guide.md) <br>
- [Research and synchronization workflows](references/workflows.md) <br>
- [Public bootstrap source](https://github.com/super21-bat/trek-agent-control) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May perform authenticated remote MCP reads and writes to Trek travel data when the user provides a Trek Agent Key.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
