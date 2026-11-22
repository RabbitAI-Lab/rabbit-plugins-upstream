## Description:

Create, search, and manage Bear notes via grizzly CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Bear users use this skill to create, read, append to, tag, search, and configure Bear notes on macOS through the grizzly CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to install a mutable third-party grizzly CLI release.

Mitigation: Review the grizzly CLI source and pin a trusted version before installing.

Risk: The Bear API token may be stored in a plaintext file.

Mitigation: Treat the token like a password, store it with owner-only permissions, avoid writing real tokens into shell history, and rotate it if exposed.

## Reference(s):

- [Bear](https://bear.app)
- [grizzly CLI Go module](https://github.com/tylerwince/grizzly)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/bear-notes)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and TOML configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some commands can return JSON when grizzly callbacks are enabled.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
