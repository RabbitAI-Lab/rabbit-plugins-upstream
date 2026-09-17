## Description:

Browse AI lets an agent read, create, and update Browse AI data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Browse AI robots and tasks through an OOMOL-connected account, including listing robots, inspecting task data, starting tasks, and updating robot cookies when explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote shell installer commands for the oo CLI.

Mitigation: Use a verified, versioned installer or trusted package-manager path before running setup commands; install only from an OOMOL endpoint the user trusts.

Risk: The skill can update Browse AI robot cookies, which changes Browse AI state.

Mitigation: Confirm the exact robot, payload, and expected effect with the user before running update_robot_cookies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-browse-ai)
- [Browse AI homepage](https://www.browse.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Browse AI connection page](https://console.oomol.com/app-connections?provider=browse_ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are JSON when run with --json.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
