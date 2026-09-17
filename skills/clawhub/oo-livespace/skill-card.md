## Description:

Livespace (livespace.io). Use this skill for ANY Livespace request: reading, creating, updating, and deleting data through OOMOL's Livespace connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external operators, and developers use this skill to manage Livespace CRM records through an OOMOL-connected account. It supports reading, listing, searching, creating, updating, and deleting companies, deals, people, todos, and users with schema inspection before actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in setup instructions could execute changing external code on the user's machine.

Mitigation: Prefer OOMOL's official installation documentation or a package-manager/release flow with version and integrity checks before installing the oo CLI.

Risk: Write and delete actions can make real changes to Livespace CRM data.

Mitigation: Confirm exact targets, payloads, and expected effects with the user before allowing write or destructive actions.

## Reference(s):

- [ClawHub Livespace Skill](https://clawhub.ai/oomol/skills/oo-livespace)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Livespace Homepage](https://www.livespace.io/)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Livespace connector responses as JSON with data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
