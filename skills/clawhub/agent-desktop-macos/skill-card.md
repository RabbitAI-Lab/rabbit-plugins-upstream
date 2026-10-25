## Description:

Guides agents using agent-desktop to automate macOS apps, manage permissions, navigate interface surfaces, and troubleshoot failed actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lahfir](https://clawhub.ai/user/lahfir)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this guide to operate macOS desktop apps through agent-desktop, grant only necessary permissions, and diagnose automation failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Accessibility, Screen Recording, and Automation grants can expose or control on-screen content.

Mitigation: Grant each permission only to trusted launching apps and only when the task needs it.

Risk: Physical input or notification actions can affect the wrong window or item.

Mitigation: Use headed mode only when needed; confirm the target and observe the result before continuing.

## Reference(s):

- [agent-desktop-macos on ClawHub](https://clawhub.ai/lahfir/skills/agent-desktop-macos)
- [macOS troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires macOS 13 or later and the agent-desktop CLI.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; skill frontmatter says 0.8.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
