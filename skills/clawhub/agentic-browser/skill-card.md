## Description: <br>
Browser automation for AI agents via inference.sh, supporting navigation, element interaction with @e refs, screenshots, video recording, JavaScript execution, uploads, and proxy-enabled sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation-focused agents use this skill to browse websites, inspect page state, interact with UI elements, fill forms, capture screenshots or videos, and extract web content through controlled browser sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables high-capability authenticated browsing, cookie handling, JavaScript execution, uploads, recording, and proxy use. <br>
Mitigation: Install only from a trusted publisher, automate only sites and accounts where use is authorized, review JavaScript before execution, and close sessions promptly. <br>
Risk: Screenshots, videos, uploaded files, and authenticated sessions can expose sensitive account or page data. <br>
Mitigation: Avoid recording sensitive pages, upload only approved files, keep generated media in approved storage, and avoid exporting or logging cookies. <br>
Risk: Proxy support and automated interaction can be misused to evade site controls or rate limits. <br>
Mitigation: Use trusted proxies only, follow site terms and internal policies, and do not use the skill for access-control, geographic, or rate-limit evasion. <br>


## Reference(s): <br>
- [Agent Browser on ClawHub](https://clawhub.ai/okaris/skills/agentic-browser) <br>
- [inference.sh Sessions](https://inference.sh/docs/extend/sessions) <br>
- [inference.sh Multi-function Apps](https://inference.sh/docs/extend/multi-function-apps) <br>
- [Command Reference](references/commands.md) <br>
- [Snapshot and Refs](references/snapshot-refs.md) <br>
- [Authentication Patterns](references/authentication.md) <br>
- [Session Management](references/session-management.md) <br>
- [Video Recording](references/video-recording.md) <br>
- [Proxy Support](references/proxy-support.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; runtime calls return JSON plus screenshots or video files when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Browser sessions may retain cookies and page state until closed; @e element refs should be refreshed after navigation or page changes.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
