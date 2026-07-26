## Description: <br>
Things Mac helps agents manage Things 3 on macOS through the `things` CLI, including adding or updating todos and reading inbox, today, upcoming, search, project, area, and tag data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and users with Things 3 on macOS use this skill to let an agent inspect local Things lists, search tasks, and propose or run `things` CLI commands for adding and updating todos. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local Things database reads may require Full Disk Access on macOS. <br>
Mitigation: Try normal read commands first, then grant Full Disk Access only to the intended calling app if needed. <br>
Risk: Write and update commands can modify Things tasks and may require a Things auth token. <br>
Mitigation: Keep `THINGS_AUTH_TOKEN` private and use `--dry-run` before uncertain write or update commands. <br>


## Reference(s): <br>
- [Things Mac on ClawHub](https://clawhub.ai/steipete/skills/things-mac) <br>
- [things3-cli repository](https://github.com/ossianhempel/things3-cli) <br>
- [things3-cli Go module](https://pkg.go.dev/github.com/ossianhempel/things3-cli/cmd/things) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [macOS-only; commands require Things 3 and the `things` CLI, and local database reads may require Full Disk Access.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
