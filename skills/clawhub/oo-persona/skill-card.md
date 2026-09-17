## Description:

Operates Persona through an OOMOL-connected account to read, create, list, and update Persona inquiries via the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with Persona inquiries from an OOMOL-connected account, including creating inquiries from templates, retrieving or listing inquiries, and updating supported inquiry fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can create local execution risk during setup.

Mitigation: Prefer official, verifiable installation steps and review install commands before running them.

Risk: Dynamic Persona fields interpolated directly into shell commands can produce malformed or unsafe command payloads.

Mitigation: Use a JSON file payload with @path/to/file.json for dynamic fields.

Risk: Persona create and update actions change account data.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Persona skill page](https://clawhub.ai/oomol/skills/oo-persona)
- [Persona homepage](https://withpersona.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before action payloads and user confirmation before Persona write actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
