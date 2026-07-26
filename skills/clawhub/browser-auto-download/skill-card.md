## Description: <br>
Browser Auto Download helps agents download files from dynamic web pages by using browser automation for auto-triggered downloads, multi-step navigation, platform-specific selection, and fallback button clicking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaronxx](https://clawhub.ai/user/aaronxx) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, engineers, and agent operators use this skill when curl or wget cannot reliably retrieve a file because the download depends on browser-rendered content, page navigation, platform-specific choices, or click-triggered browser download events. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaronxx/skills/browser-auto-download) <br>
- [Publisher profile](https://clawhub.ai/user/aaronxx) <br>
- [README](README.md) <br>
- [Quick start guide](QUICKSTART.md) <br>
- [User guide](USER_GUIDE.md) <br>
- [Playwright](https://playwright.dev/) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash and Python examples; runtime script output includes progress on stderr and a JSON download result on stdout.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill saves downloaded files locally and may save screenshots, HTML, and text in a local debug folder when debug mode is enabled. Use trusted URLs, verify downloaded installers or archives before execution, avoid debug mode on logged-in or sensitive pages, and delete debug artifacts when no longer needed.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
