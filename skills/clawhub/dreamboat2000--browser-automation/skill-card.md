## Description:

Automate web browser interactions using natural language via CLI commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dreamboat2000](https://clawhub.ai/user/dreamboat2000)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to navigate websites, click and fill page elements, extract structured web data, capture screenshots, and manage browser sessions from CLI commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser sessions and cookies can persist in the Chrome profile.

Mitigation: Use an isolated browser profile and avoid real credentials or sensitive accounts unless the profile lifecycle is controlled.

Risk: Remote Browserbase mode may be selected automatically when Browserbase credentials are present.

Mitigation: Check the environment before use and confirm whether local or remote browser execution is active.

Risk: Browser automation can expose a browser-control port and operate on internal or regulated sites.

Mitigation: Run only in a trusted environment, avoid internal or regulated targets unless approved, and verify the source code and dependencies behind the global browser command.

Risk: The skill can download files without strong upfront controls.

Mitigation: Treat downloaded files as untrusted and review or scan them before opening or using them.

## Reference(s):

- [Browser Automation ClawHub Release](https://clawhub.ai/dreamboat2000/skills/browser-automation)
- [Browser Automation Examples](EXAMPLES.md)
- [Browser Automation CLI Reference](REFERENCE.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash command examples; browser commands return JSON and can create PNG screenshots or downloaded files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Screenshots are written under ./agent/browser_screenshots/ and downloads under ./agent/downloads/ when the browser CLI performs those actions.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
