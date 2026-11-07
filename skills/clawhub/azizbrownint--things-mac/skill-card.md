## Description:

Add, update, list, search, or inspect Things 3 todos, inbox, today, projects, areas, and tags on macOS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers on macOS use this skill to inspect and manage local Things 3 tasks through things3-cli, including listing, searching, adding, and updating todos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Granting Full Disk Access to Terminal or OpenClaw.app can expose more local data than Things task data.

Mitigation: Grant Full Disk Access only when database reads require it, limit it to the intended calling app, and revoke it afterward.

Risk: Installing things3-cli with an unpinned latest version can introduce unexpected behavior changes.

Mitigation: Review or pin the things3-cli version before installation in managed or sensitive environments.

Risk: Passing auth tokens directly in commands can expose them through shell history or process listings.

Mitigation: Use THINGS_AUTH_TOKEN instead of command-line token arguments for update operations.

## Reference(s):

- [things3-cli GitHub repository](https://github.com/ossianhempel/things3-cli)
- [ClawHub things-mac skill page](https://clawhub.ai/azizbrownint/skills/things-mac)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [macOS-only; commands target a local Things 3 database and the Things URL scheme.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
