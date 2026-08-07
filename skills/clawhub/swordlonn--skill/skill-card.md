## Description:

Watchitai enables AI agents to start cross-platform screen sharing, optional remote desktop control, and real-time monitoring through browser-accessible WebRTC sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[swordlonn](https://clawhub.ai/user/swordlonn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent users use Watchitai to create browser-accessible screen-sharing sessions and, when explicitly permitted, remote keyboard and mouse control for troubleshooting, monitoring, or collaborative operation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill downloads and runs a remote binary with screen viewing and optional keyboard and mouse control privileges.

Mitigation: Install only when the WatchItAI publisher is trusted, prefer view-only sessions, and grant control permissions only for explicit remote-control use cases.

Risk: Screen-sharing sessions can expose sensitive information visible on the local display.

Mitigation: Hide passwords, private keys, and confidential content before sharing, and stop the bridge service when the session is finished.

Risk: Account authorization can make config.json sensitive if credentials are written there.

Mitigation: Treat config.json as sensitive after authorization and avoid sharing or publishing the installed skill directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/swordlonn/skills/skill)
- [WatchItAI homepage](https://watchitai.net)
- [WatchItAI host page](https://watchitai.net/host)
- [WatchItAI downloads](https://watchitai.net/downloads/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and browser session links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit a marked WatchItAI session URL for agents to present as a Markdown link.]

## Skill Version(s):

0.1.1 (source: server release metadata; artifact frontmatter and package metadata report 2.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
