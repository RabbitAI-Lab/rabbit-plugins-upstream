## Description:

Control D (controld.com). Use this skill for ANY Control D request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Control D profiles, DNS rules, service discovery, and API-detected IP troubleshooting through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes direct execution of remote installer scripts.

Mitigation: Review the setup path before installation and prefer a verified or package-manager installation of the oo CLI.

Risk: Write and destructive actions can change or delete Control D DNS rules.

Mitigation: Confirm the exact payload, target profile, and expected effect with the user before running write or destructive actions.

Risk: Control D actions are routed through OOMOL-connected credentials.

Mitigation: Use the skill only when the user is comfortable using OOMOL-managed connection credentials for Control D operations.

## Reference(s):

- [Control D homepage](https://controld.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Control D skill on ClawHub](https://clawhub.ai/oomol/skills/oo-control-d)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
