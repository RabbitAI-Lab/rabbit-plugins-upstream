## Description:

Agent states such as thinking, waiting, idle, and error are synced to a workled device over MCP, and the skill can configure light effects and touch macros for the device.

This skill is ready for commercial/non-commercial use.

## Publisher:

[git-hub-cloud](https://clawhub.ai/user/git-hub-cloud)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use workled to connect an MCP-capable hardware LED and touch-pad device to supported agent clients, so agent states can be reflected visually and touch macros can be configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation can create persistent hooks or plugins in supported agent clients.

Mitigation: Review the installer output and target client before installation, and use the documented uninstall flow when removing the skill.

Risk: Touch macros can handle password-like values and may communicate over the default HTTP MCP URL.

Mitigation: Avoid storing real passwords in touch macros, especially when using the default HTTP MCP endpoint.

Risk: Some installation paths may require administrator or root approval.

Mitigation: Confirm any elevated approval request before proceeding and restrict installation to the intended client.

## Reference(s):

- [workled Skill Page](https://clawhub.ai/git-hub-cloud/skills/workled)
- [Device Setup Reference](references/device_setup.md)
- [Macro Format Reference](references/macro_format.md)
- [Video Demo](https://www.bilibili.com/video/BV1FK4k6WEKe)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool arguments for LED state, brightness, effect, and touch macro configuration.]

## Skill Version(s):

0.1.30 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
