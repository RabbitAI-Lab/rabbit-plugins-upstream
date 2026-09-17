## Description:

Statamic (statamic.com). Use this skill for Statamic account operations such as listing, creating, updating, and deleting site licenses through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Statamic site licenses from an OOMOL-connected Statamic account. It supports read, write, and destructive account actions while directing the agent to inspect live action schemas before sending payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions pipe remote installer scripts directly into the shell.

Mitigation: Review and verify the installer source before running setup; prefer official package-manager or signed release installation paths when available.

Risk: Write and destructive actions can change or delete Statamic site-license data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before creating, updating, or deleting a site license.

## Reference(s):

- [Statamic homepage](https://statamic.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-statamic)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before write or destructive Statamic actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
