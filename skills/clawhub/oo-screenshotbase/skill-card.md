## Description:

Helps an agent operate screenshotbase through the OOMOL-connected oo CLI to check quota status and capture webpages as hosted screenshots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run screenshotbase connector actions through an OOMOL-connected account, including webpage screenshot capture and quota checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer scripts for the oo CLI.

Mitigation: Treat CLI setup as privileged software installation, prefer official version-pinned instructions, and avoid piping remote scripts directly into a shell.

Risk: Screenshot capture returns hosted results and may consume connected account quota.

Mitigation: Confirm screenshot targets before capture and check quota or billing status when usage limits may affect the request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-screenshotbase)
- [screenshotbase homepage](https://screenshotbase.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, PowerShell commands, text URLs, and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON connector responses that include hosted screenshot URLs, quota data, and execution metadata.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
