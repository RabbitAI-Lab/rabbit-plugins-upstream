## Description: <br>
Automate web browser interactions using natural language via CLI commands for browsing, page navigation, data extraction, screenshots, form filling, button clicks, and web application interaction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[peytoncasper](https://clawhub.ai/user/peytoncasper) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to drive a browser through a CLI, navigate websites, perform natural-language page actions, extract structured page data, take screenshots, and manage browser sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad browser-control authority, including persistent sessions, downloads, and possible remote Browserbase sessions. <br>
Mitigation: Use isolated browser profiles, avoid saving passwords, and confirm before submissions, purchases, account changes, downloads, or remote browser sessions. <br>
Risk: Stored browser profiles, screenshots, and downloads may retain sensitive browsing data after use. <br>
Mitigation: Clear .chrome-profile, agent/browser_screenshots, and agent/downloads when the session is finished. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/peytoncasper/skills/agent-browser-stagehand) <br>
- [Browser Automation Examples](EXAMPLES.md) <br>
- [Browser Automation CLI Reference](REFERENCE.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance, files] <br>
**Output Format:** [CLI commands, JSON or text command results, PNG screenshots, and downloaded files when browser actions create them] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands require setup of Chrome, Node.js dependencies, the browser CLI link, and ANTHROPIC_API_KEY; Browserbase is used when configured.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
