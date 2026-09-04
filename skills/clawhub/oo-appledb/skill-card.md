## Description:

AppleDB (appledb.dev) supports searching and reading Apple device and operating system build data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query AppleDB device and operating system build records through the OOMOL-connected oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions can execute an unverified remote installer for the oo CLI.

Mitigation: Install the oo CLI only through a verified, pinned, or trusted package-manager path before using this skill.

Risk: The allowed oo CLI action pattern is broader than the four documented AppleDB read actions.

Mitigation: Limit use to get_device, get_os_build, search_devices, and search_os_builds unless the user explicitly approves another action.

## Reference(s):

- [AppleDB homepage](https://appledb.dev)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub AppleDB skill page](https://clawhub.ai/oomol/skills/oo-appledb)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include AppleDB connector output returned as JSON through the oo CLI.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
