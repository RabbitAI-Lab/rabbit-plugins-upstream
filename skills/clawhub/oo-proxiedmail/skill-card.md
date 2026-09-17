## Description:

ProxiedMail helps an agent operate ProxiedMail through an OOMOL-connected account for reading, creating, and updating proxy email data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent inspect ProxiedMail schemas, list or read proxy email data, and create or update proxy email bindings through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented setup path includes installer one-liners that execute remote code from OOMOL's installer endpoint.

Mitigation: Review the skill before installation and prefer a signed, versioned, or checksum-verified oo CLI installation path.

Risk: Write actions can create or update ProxiedMail proxy email bindings.

Mitigation: Confirm the exact action payload and expected effect with the user before running write actions.

## Reference(s):

- [ProxiedMail Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-proxiedmail)
- [ProxiedMail Homepage](https://proxiedmail.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write actions require confirmation of the exact payload and effect.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
