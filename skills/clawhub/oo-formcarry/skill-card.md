## Description:

Formcarry (formcarry.com). Use this skill for Formcarry requests that read, create, update, or delete Formcarry data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Formcarry forms and submissions through the `oo` CLI, including schema inspection, form creation, submission listing, and confirmed deletion of forms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded content directly into a shell.

Mitigation: Review installer commands before use and prefer a verified, versioned, signed, or checksum-validated oo CLI installation source.

Risk: Form creation and deletion can change or remove Formcarry resources.

Mitigation: Inspect the live action schema, check payloads carefully, and require explicit user confirmation before create or delete actions.

## Reference(s):

- [Formcarry homepage](https://formcarry.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-formcarry)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and return JSON responses from connector actions.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
