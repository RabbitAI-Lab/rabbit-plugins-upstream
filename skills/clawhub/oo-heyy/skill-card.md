## Description:

Heyy lets agents read, create, and update Heyy data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Heyy contacts, labels, channels, and attributes from an OOMOL-connected account. It supports read actions and confirmed write actions for creating or updating Heyy CRM data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Review the oo CLI installation path first, prefer official versioned downloads, check signatures or checksums when available, and avoid direct pipe-to-shell execution.

Risk: Write actions can create or update Heyy contacts, labels, and attributes.

Mitigation: Confirm the exact payload and intended effect with the user before running any action tagged write.

Risk: Connector request shapes may change over time.

Mitigation: Inspect the live action schema with oo connector schema before constructing each request payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-heyy)
- [Heyy homepage](https://heyy.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Heyy connection settings](https://console.oomol.com/app-connections?provider=heyy)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
