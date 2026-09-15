## Description:

Anchor Browser lets an agent operate Anchor Browser through the OOMOL-connected oo CLI for project metadata, billing information, and browser session actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Anchor Browser action schemas, retrieve project and billing details, and start browser sessions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute code on the local machine.

Mitigation: Review the installer first or prefer an official package manager or signed release, and run setup only when the oo CLI is actually missing.

Risk: Starting a browser session changes Anchor Browser state and may create connection URLs.

Mitigation: Confirm the exact payload and effect with the user before running the start_browser_session action.

## Reference(s):

- [Anchor Browser homepage](https://anchorbrowser.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Anchor Browser connection settings](https://console.oomol.com/app-connections?provider=anchor_browser)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-anchor-browser)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return CDP and live-view connection URLs when starting browser sessions.]

## Skill Version(s):

1.0.2 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
