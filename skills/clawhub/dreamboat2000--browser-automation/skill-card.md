## Description: <br>
Automates browser navigation, web page interaction, data extraction, screenshots, form filling, button clicks, and web application workflows through natural-language CLI commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dreamboat2000](https://clawhub.ai/user/dreamboat2000) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and agent operators use this skill to drive a local Chrome or Browserbase-backed browser for website navigation, form filling, page observation, structured extraction, screenshots, downloads, and debugging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can drive a browser broadly, including external sites, localhost, internal networks, and authenticated sessions. <br>
Mitigation: Review requested actions before execution, use a disposable browser profile, and avoid sensitive accounts unless session persistence is explicitly intended. <br>
Risk: Browserbase remote browsing can be selected automatically when Browserbase API keys are present. <br>
Mitigation: Remove Browserbase keys when remote browsing is not intended and verify the active environment before running browser tasks. <br>
Risk: The browser may persist cookies and saved session state in .chrome-profile. <br>
Mitigation: Use isolated profiles for sensitive work and clear the profile after tasks that involve credentials or private sites. <br>
Risk: Screenshots and downloads can save local files that may contain sensitive or untrusted content. <br>
Mitigation: Monitor and clean ./agent/browser_screenshots and ./agent/downloads, and verify downloaded files before opening or reusing them. <br>
Risk: Setup commands rely on npm install and npm link, while the release evidence indicates the CLI/package source should be verified before relying on setup. <br>
Mitigation: Inspect the package and CLI source before installation, then run setup only in an environment appropriate for untrusted dependencies. <br>


## Reference(s): <br>
- [Browser Automation Examples](EXAMPLES.md) <br>
- [Browser Automation CLI Reference](REFERENCE.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON, files, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON command outputs, screenshots, and downloaded files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may create persistent browser profiles, screenshots under ./agent/browser_screenshots, and downloaded files under ./agent/downloads.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
