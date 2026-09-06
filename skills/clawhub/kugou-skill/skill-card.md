## Description:

Kugou helps agents use kugou-cli to search Kugou Music, get recommendations, view favorites and listening stats, create playlists, and control the local Kugou desktop client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shamo88](https://clawhub.ai/user/shamo88)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent perform Kugou Music searches, recommendations, playlist operations, account-aware library queries, and optional desktop-client playback control through documented shell commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to handle reusable Kugou account session secrets.

Mitigation: Prefer QR login, avoid pasting base64 secrets into chat or shell history unless necessary, and confirm login state before running account-backed music commands.

Risk: The npm installation flow can modify multiple agent skill folders during postinstall or install commands.

Mitigation: Review the package and installation target before installing, and run installation in a controlled environment when agent skill directories are sensitive.

Risk: Automatic update checks can contact the npm registry from environments where outbound package-registry access is sensitive.

Mitigation: Review or disable automatic update checks using the documented environment variable or command flag in restricted networks.

Risk: Desktop control operations depend on a logged-in Kugou client and are unsupported outside Windows and macOS.

Mitigation: Detect client availability before presenting playback links and fall back to query-only or cloud playlist workflows when local control is unavailable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/shamo88/skills/kugou-skill)
- [Authentication Commands](references/auth.md)
- [Music Commands](references/music.md)
- [Desktop Client Control](references/control.md)
- [Installation Commands](references/install.md)
- [Update Behavior](references/update.md)
- [Output Format](references/output-format.md)
- [Error Handling](references/error-handling.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-aware response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include song or playlist tables, QR-code presentation guidance, and follow-up prompts for login or playback confirmation.]

## Skill Version(s):

0.1.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
