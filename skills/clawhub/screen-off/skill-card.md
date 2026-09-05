## Description:

Toggle any macOS display on/off by ID, name, or index.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mfang0126](https://clawhub.ai/user/mfang0126)

### License/Terms of Use:

MIT

## Use Case:

Developers and macOS users use this skill to list connected displays and turn a specific screen on or off from a terminal or agent workflow by display ID, index, or name.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Force or permanent display changes can leave a Mac without a visible display.

Mitigation: Avoid --force unless another display, remote access, or a recovery path is available, and use --permanent only when the display state should survive reboot.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mfang0126/skills/screen-off)
- [zy0816/ScreenOff](https://github.com/zy0816/ScreenOff)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with shell command examples and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [macOS-only; requires Python 3.8+ and CoreGraphics/SkyLight display APIs.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
