## Description:

Computer use for Windows, macOS, Linux and WSL. Screenshot the screen, list windows, click buttons by name, close/focus apps, type text, press keys, click by coordinates. No installs on Windows/macOS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[brayanjeshua](https://clawhub.ai/user/brayanjeshua)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can use this skill to inspect and operate desktop applications on Windows, macOS, Linux, and WSL, including finding and activating controls by their visible names.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags a mismatch between a reported install command and the skill’s no-install claim for Windows and macOS; the scan is incomplete.

Mitigation: Review the installation instructions and confirm the setup for the intended platform before proceeding; treat the scan result as incomplete.

Risk: Desktop actions can affect open applications and their contents.

Mitigation: Check the current screen and visible control labels before acting, and avoid closing unsaved work or entering secrets.

## Reference(s):

- [Desktop Pilot on ClawHub](https://clawhub.ai/brayanjeshua/skills/desktop-pilot)

## Skill Output:

**Output Type(s):** [Text, Files, Shell commands, Guidance]

**Output Format:** [Text listings and status messages, PNG screenshots, and desktop actions invoked through shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can inspect windows and controls, then focus, click, type, send key combinations, or capture screenshots on supported desktops.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
