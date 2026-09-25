## Description:

Enables an agent to inspect and control desktop applications using screenshots, clicks, typing, keyboard shortcuts, scrolling, and app launches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[topgemstoken](https://clawhub.ai/user/topgemstoken)

### License/Terms of Use:

Apache-2.0

## Use Case:

Users and developers can direct an agent to inspect the screen and automate desktop applications when command-line or browser tools cannot reach the relevant interface.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Screen access and desktop control may expose sensitive documents, passwords, messages, or payment details.

Mitigation: Install only when desktop control is intended; avoid sensitive screens and have the user enter passwords or one-time codes directly.

Risk: AppleScript provides broad local automation on macOS.

Mitigation: Treat AppleScript commands as privileged actions and review their intended effect before running them.

Risk: Untrusted application names may be unsafe in the Linux launch path.

Mitigation: Use only trusted, explicitly chosen application names on Linux until the launch path is tightened.

## Reference(s):

- [Computer Control skill on ClawHub](https://clawhub.ai/topgemstoken/skills/computer-control)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Text or JSON diagnostics and local PNG screenshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Desktop actions require the applicable operating-system permissions.]

## Skill Version(s):

1.0.2 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
