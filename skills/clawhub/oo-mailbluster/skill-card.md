## Description:

MailBluster (mailbluster.com). Use this skill for MailBluster requests including reading, creating, updating, and deleting data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate MailBluster through an OOMOL-connected account, including lead creation, retrieval, updates, deletion, and custom-field listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer scripts for the oo CLI.

Mitigation: Review the installer step before use and prefer a pinned, verified release or documented package manager path.

Risk: Write and destructive actions can create, update, or delete MailBluster lead data.

Mitigation: Confirm the exact payload, target lead hash, and intended effect before approving write or delete actions.

## Reference(s):

- [MailBluster homepage](https://mailbluster.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON responses from the oo CLI when run with --json.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
