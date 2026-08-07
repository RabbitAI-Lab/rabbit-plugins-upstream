## Description: <br>
Drive Herdr terminal multiplexer panes from Telegram: spawn a dedicated tab, send prompts to any CLI agent, wait for done/blocked, and relay transcripts back. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mentholmike](https://clawhub.ai/user/mentholmike) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let Telegram users start and steer Herdr-managed CLI agent sessions, monitor status, and receive transcript output without taking over existing interactive panes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Telegram-connected users can start and steer local CLI agents through the gateway. <br>
Mitigation: Install only when those Telegram users are intended to control local CLI agents, and prefer the Herdr pane flow for visibility and auditability. <br>
Risk: Injecting text into unrelated interactive panes can disrupt user work or create prompt-injection exposure. <br>
Mitigation: Drive only panes and tabs spawned by the skill by default, require explicit pane IDs for other panes, and parse pane and tab IDs from Herdr JSON responses. <br>
Risk: Headless one-shot agent runs provide less visibility than pane-based sessions. <br>
Mitigation: Use the headless shortcut only for simple prompts with trusted agent binaries; use Herdr panes for persistent sessions, follow-ups, or live monitoring. <br>


## Reference(s): <br>
- [Herdr terminal multiplexer](https://github.com/mentholmike/herdr) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and fenced terminal transcript excerpts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Telegram output may need line-aware chunking for message limits; terminal output should be relayed without raw ANSI escape sequences.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
