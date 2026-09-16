## Description:

GoDial lets an agent list accounts, lists, and contacts, fetch individual contacts, and create contacts in GoDial through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect GoDial accounts, lists, and contacts, and to create contacts in selected lists through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path recommends remote shell installer commands for the OOMOL oo CLI.

Mitigation: Prefer a verified or package-managed install path when available, or inspect and verify the installer before running it.

Risk: Connecting GoDial requires trusting the OOMOL account connection flow for credential handling.

Mitigation: Install only after accepting the OOMOL connection model and use the documented connection URL only when authentication or scope errors require it.

Risk: The create_contact action can add records to a GoDial list.

Mitigation: Confirm the target list, exact contact payload, and expected effect before running the write action.

## Reference(s):

- [GoDial homepage](https://godial.cc)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [GoDial skill on ClawHub](https://clawhub.ai/oomol/skills/oo-godial)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions can be run directly; contact creation requires confirmation of the exact payload and effect.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
