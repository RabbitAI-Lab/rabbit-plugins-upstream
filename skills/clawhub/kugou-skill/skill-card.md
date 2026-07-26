## Description: <br>
酷狗 is a Kugou Music assistant skill for searching songs, generating recommendations, viewing charts and account music data, and creating playlists through the `kugou-cli` CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shamo88](https://clawhub.ai/user/shamo88) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to let an agent operate Kugou Music workflows, including song search, personalized recommendations, favorites, recent plays, listening statistics, charts, QR or secret-based login, and user-confirmed playlist creation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles a Kugou session secret and can access private account data such as favorites, recent plays, listening statistics, and playlist creation. <br>
Mitigation: Install only if the user trusts the `@kg-ai/kugou-skill` package, avoid exposing secrets in shared terminals or logs, and run account-data commands only after the user explicitly requests them. <br>
Risk: The CLI can check for and apply global npm package updates during normal use. <br>
Mitigation: Review update behavior before installation, disable automatic update checks where appropriate with `--no-update-check` or `KUGOU_CLI_NO_UPDATE_CHECK=1`, and confirm updates before running global installs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shamo88/skills/kugou-skill) <br>
- [Authentication commands](artifact/references/auth.md) <br>
- [Music commands](artifact/references/music.md) <br>
- [Installation commands](artifact/references/install.md) <br>
- [Update commands](artifact/references/update.md) <br>
- [Output format](artifact/references/output-format.md) <br>
- [Error handling](artifact/references/error-handling.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown responses derived from JSON CLI output, with shell commands for setup and authentication workflows.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands write JSON to stdout and errors to stderr; music results should be presented as Markdown links when play URLs are available.] <br>

## Skill Version(s): <br>
0.1.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
