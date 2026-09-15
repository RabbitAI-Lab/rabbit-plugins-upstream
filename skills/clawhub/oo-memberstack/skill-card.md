## Description:

Memberstack (memberstack.com) supports reading, creating, updating, and deleting Memberstack data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Memberstack connector schemas and run JSON-based actions against an OOMOL-connected Memberstack account. It supports member lookup, listing, creation, updates, plan changes, token verification, and deletion workflows with confirmation requirements for write and destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute immediately on the user's machine.

Mitigation: Prefer a signed or package-manager install, a pinned release, or a manually downloaded installer with checksum or signature verification before running the oo CLI.

Risk: Write and destructive connector actions can modify or delete Memberstack members, plans, profile data, and related subscription cleanup settings.

Mitigation: Inspect the live action schema, confirm the exact payload and target with the user, and require explicit approval before member updates, free-plan removals, or deletions.

## Reference(s):

- [ClawHub Memberstack Skill Page](https://clawhub.ai/oomol/skills/oo-memberstack)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Memberstack Homepage](https://www.memberstack.com/)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the oo CLI connector and may return JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
