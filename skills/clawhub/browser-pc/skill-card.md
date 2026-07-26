## Description: <br>
Automate web browser interactions using natural language via CLI commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[peytoncasper](https://clawhub.ai/user/peytoncasper) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to navigate websites, interact with page elements, extract structured page data, take screenshots, and run browser-based workflows from the command line. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives the agent broad live-browser control, including navigation, form interaction, screenshots, and data extraction. <br>
Mitigation: Review planned browser actions before sensitive use, prefer non-sensitive test accounts, and inspect screenshots or extracted data before relying on results. <br>
Risk: Browserbase remote mode may be selected automatically when Browserbase credentials are configured. <br>
Mitigation: Confirm whether Browserbase mode is active before handling private data or credentials. <br>
Risk: The local browser profile can preserve cookies, sessions, and saved state between runs. <br>
Mitigation: Use isolated or cleared browser profiles for sensitive workflows and avoid entering real passwords unless necessary. <br>
Risk: Browser actions can automatically download files into ./agent/downloads/. <br>
Mitigation: Treat downloaded files as untrusted until verified, and scan or inspect them before opening or using them. <br>


## Reference(s): <br>
- [Browser Automation CLI on ClawHub](https://clawhub.ai/peytoncasper/skills/browser-pc) <br>
- [Browser Automation Examples](EXAMPLES.md) <br>
- [Browser Automation CLI Reference](REFERENCE.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; CLI commands return JSON and may create screenshot or download files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Screenshots are written under ./agent/browser_screenshots/ and downloads under ./agent/downloads/ when those commands or browser actions are used.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
