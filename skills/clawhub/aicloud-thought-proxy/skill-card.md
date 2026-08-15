## Description:

AIcloud Thought Proxy lets an agent drive a user's browser to coordinate with web-based AI chat services while the local agent performs execution tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[georgechou17](https://clawhub.ai/user/georgechou17)

### License/Terms of Use:

MIT-0 (MIT No Attribution)

## Use Case:

Developers and agent users use this skill to offload planning, coding, and reasoning to a logged-in web AI while the local agent performs browser, file, shell, and download tasks with user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control logged-in browser sessions.

Mitigation: Use a dedicated browser profile or account, require user confirmation for key actions, and remove browser-control tooling when finished.

Risk: User requests, execution results, or copied content may be relayed to third-party AI sites.

Mitigation: Avoid sending secrets, private files, credentials, or regulated data, and review each relay before submission.

Risk: The workflow may install or configure browser-control tools and drivers.

Mitigation: Install tools only with explicit user consent, prefer official release sources, and remove the extension, MCP configuration, and installed drivers when no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/georgechou17/skills/aicloud-thought-proxy)
- [Server-resolved GitHub source](https://github.com/GeorgeChou17/aicloud-thought-proxy)
- [AI model and mode catalog](references/ai-models.md)
- [Browser engine detection guide](references/browser-detection.md)
- [Chromium browser automation guide](references/chromium-automation.md)
- [Gecko browser automation guide](references/gecko-automation.md)
- [Browser control tool installation guide](references/tool-installation.md)
- [mcp-chrome releases](https://github.com/hangwin/mcp-chrome/releases)
- [GeckoDriver releases](https://github.com/mozilla/geckodriver/releases)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May relay prompts and execution summaries between a local agent and third-party web AI services.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
