## Description:

酷狗 helps agents search and recommend Kugou Music tracks, view charts and listening data, manage favorites and playlists, adjust recommendation preferences, and control the local Kugou client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shamo88](https://clawhub.ai/user/shamo88)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to route music requests through Kugou CLI workflows for search, recommendations, charts, playlist management, account login, and local client playback control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a globally installed Kugou CLI that can access the user's Kugou account, local client, browser, and listening data.

Mitigation: Install only after trusting the npm publisher and run commands in an environment where account and local-client access are acceptable.

Risk: The skill supports direct login with a base64 account secret.

Mitigation: Prefer QR login, paste secrets only when necessary, quote secret values in shell commands, and avoid sharing or logging the secret.

Risk: The update flow can replace the installed CLI with @latest.

Mitigation: Review update output and approve updates explicitly before running forced or @latest installs.

Risk: The artifact includes troubleshooting guidance that can lead users toward disabling Windows Memory Integrity.

Mitigation: Do not disable Windows Memory Integrity for this skill; prefer client updates or safer environment fixes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shamo88/skills/kugou-skill)
- [Authentication commands](references/auth.md)
- [Music commands](references/music.md)
- [Control commands](references/control.md)
- [Install commands](references/install.md)
- [Update commands](references/update.md)
- [Output format and display rules](references/output-format.md)
- [Error handling](references/error-handling.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with inline shell commands and JSON-aware result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may depend on Kugou account state, local client availability, and CLI JSON responses.]

## Skill Version(s):

0.1.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
