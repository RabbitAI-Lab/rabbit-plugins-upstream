## Description: <br>
Automate web browser interactions using natural language via CLI commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[peytoncasper](https://clawhub.ai/user/peytoncasper) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external agents use this skill to drive a browser from natural-language tasks, including navigation, page interaction, structured data extraction, screenshots, form filling, and downloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad browser control can navigate, click, type, submit forms, and interact with authenticated pages. <br>
Mitigation: Review proposed actions before execution, confirm before submitting forms or downloading files, and use the observe and screenshot commands to verify page state. <br>
Risk: Persistent browser sessions can retain cookies, saved credentials, screenshots, downloads, and cached data. <br>
Mitigation: Use a dedicated browser profile without saved passwords or sensitive accounts, and periodically clear .chrome-profile, screenshots, downloads, and cache data. <br>
Risk: The skill may use local Chrome or remote Browserbase environments depending on available configuration. <br>
Mitigation: Choose local versus Browserbase deliberately and verify environment variables before running browser tasks. <br>
Risk: The security verdict is suspicious because the skill enables broad browser automation with automatic downloads and possible remote browsing. <br>
Mitigation: Install only when the publisher is trusted and the actual CLI source and dependencies can be verified. <br>


## Reference(s): <br>
- [Browser Automation CLI Reference](artifact/REFERENCE.md) <br>
- [Browser Automation Examples](artifact/EXAMPLES.md) <br>
- [ClawHub skill page](https://clawhub.ai/peytoncasper/skills/stagehand-browser-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files, Guidance] <br>
**Output Format:** [Markdown instructions with bash commands; CLI commands return JSON and file paths for screenshots or downloads.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create a persistent Chrome profile, screenshot files, downloaded files, and cached browser state.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
