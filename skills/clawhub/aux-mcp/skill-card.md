## Description: <br>
AUX - Spotify for your AI, with vibe DJ, roast cards, party rooms, and auto-DJ through MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[brian-mwirigi](https://clawhub.ai/user/brian-mwirigi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use AUX to guide Spotify playback and discovery through MCP, including mood-based queues, playlist analysis, playlist roasts, party-room queues, auto-DJ sessions, and weekly listening summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Spotify account access and local token storage can expose playback, playlist or library actions, and listening-history features. <br>
Mitigation: Install only when comfortable granting Spotify access, keep ~/.aux-mcp/ token files private, and revoke the Spotify app or delete the token directory when no longer using the skill. <br>
Risk: Playback and party-room actions may affect the user's active Spotify device or shared queue. <br>
Mitigation: Use the skill's authentication and playback status checks before playback, and ask the user to confirm intent before queueing or playing music in shared contexts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/brian-mwirigi/skills/aux-mcp) <br>
- [AUX homepage](https://brianmunene.me/aux-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text, markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and MCP tool-use instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May surface ASCII cards from MCP tool results; Spotify Premium and an active device are required for playback.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
