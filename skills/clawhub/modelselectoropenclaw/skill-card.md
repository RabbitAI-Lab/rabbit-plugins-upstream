## Description:

ModelSelectorOpenClaw installs, repairs, verifies, or uninstalls a browser-side OpenClaw Control UI enhancement that turns the chat model picker into a two-column provider/model picker and hides the per-chat account row.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pondsi](https://clawhub.ai/user/pondsi)

### License/Terms of Use:

MIT License with mandatory attribution

## Use Case:

Developers and OpenClaw users use this skill to make large provider and model lists easier to navigate in the OpenClaw Control UI, and to install, verify, repair, or remove that local UI enhancement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer modifies local OpenClaw Control UI files by injecting one script tag and copying a browser-side asset.

Mitigation: Install only when that local UI modification is intended; review the target directory first and use the documented -Remove command to uninstall.

Risk: The browser-side enhancement performs a same-origin update check and may reload an open Control UI tab after detecting a newer server-side app shell.

Mitigation: Expect reload behavior after update detection and verify the picker state with the documented diagnostic command.

Risk: A separate GitHub watchdog mentioned in the documentation would add scheduled-task persistence, but it is not part of this ClawHub artifact.

Mitigation: Review that watchdog separately before installing it from any non-ClawHub package.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pondsi/skills/modelselectoropenclaw)
- [Publisher profile](https://clawhub.ai/user/pondsi)
- [README](artifact/README.md)
- [Changelog](artifact/CHANGELOG.md)
- [License](artifact/LICENSE)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with PowerShell command blocks and verification guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local artifact files and OpenClaw Control UI paths.]

## Skill Version(s):

1.5.1 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
