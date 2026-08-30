## Description:

VBOUT helps agents read, create, update, and delete VBOUT account, list, and contact data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate VBOUT marketing lists and contacts from an agent, including account lookup, list inspection, and contact creation, updates, retrieval, listing, or deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, and delete VBOUT contact data through the connected account.

Mitigation: Confirm the exact target, payload, and intended effect with the user before write or destructive actions.

Risk: Connector payloads may drift if VBOUT or the OOMOL connector changes its action schema.

Mitigation: Inspect the live action schema before constructing each connector payload.

Risk: First-time setup may require installing the oo CLI with an external installer.

Mitigation: Treat the installer as an external dependency and run setup only when an auth, connection, or missing-command error requires it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-vbout)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [VBOUT homepage](https://www.vbout.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON when commands are run with --json.]

## Skill Version(s):

1.0.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
